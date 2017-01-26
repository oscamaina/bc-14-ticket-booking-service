import sqlite3
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
# connect to database
db_con = sqlite3.connect("event_booking.db")
# create a temporary memory to store data
conn = db_con.cursor()
#Add Events 
def add_events():
    # create table
    conn.execute("CREATE TABLE IF NOT EXISTS event( \
                    event_id INTEGER PRIMARY KEY, event_name TEXT, start_date DATE, end_date DATE, venue TEXT ) ")

    # get user input
    print("Enter a New Event")
    print("")

    
# Number of tickets Available
#    no_of_tickets = input('Number of Tickets: ')
# Status of the event
#   status = input ('Status (Open/Closed): ')

    try:
        # run sql command and commit data to db
        event_name = input('Enter Event name: ')
    # Event Start Date
        date1_entry = input('Enter date event begins in YYYY-MM-DD format: ')
        year, month, day = map(int, date1_entry.split('-'))
        start = datetime.date(year, month, day)
    # Event End Date
        date2_entry = input('Enter date event ends in YYYY-MM-DD format: ')
        year, month, day = map(int, date2_entry.split('-'))
        end = datetime.date(year, month, day)
    # Event Description
        venue = input('Enter Venue: ')
        if end >= datetime.date.today() and start >= datetime.date.today():
            conn.execute("INSERT INTO event VALUES (null,?,?,?,?);",
                         (event_name, start, end, venue))
            db_con.commit()
            print("***.........Data saved data...........***")
        else:
            print(".........Invalid Dates. Start and End Date should be Greater than Today's date..........")
            return add_events()

    except ValueError:
        print("***......Error in saving data. Invalid Inputs. Note: Start date and End date should be greater than today...........***")
        return add_events()
#View all events or all tickets

def view_all():
    print ("Enter The Name of the table to be modified")
    name = input ("Table Name: ")
    if name == 'tickets' or name == 'Tickets' or name == 'TICKETS':

        try:      # print ("All Events (Open and Closed)")
            conn.execute("SELECT * FROM tickets")
            items = conn.fetchall()
            for row in items:
                print(row)
        except:
            print("Error occurred")
    elif name == 'events' or name == 'EVENTS' or name == 'Events':
        try:
            conn.execute("SELECT * FROM event")
            items = conn.fetchall()
            for row in items:
                print(row)
            print ("***____________All Events Displayed Above___________***")
        except:
            print ("Error in printing")
    else:
        print("Invalid Input. Try Again")
        return view_all()


def delete_event():
    
    try:
        eventid = input('Please enter ID of the event to be deleted: ')
        data = int (eventid)

        conn.execute("DELETE FROM event WHERE event_id=?", (data,))
        db_con.commit()
        print("***_______Event with ID " + eventid +" has been deleted successfully__________***")
        
    except ValueError:
        print("Invalid Input. Try Again")
        return delete_event()
#edit Data in events
def edit_event():
    

    try:
        eventid = int(input("Enter Event ID:  "))
    
      
        conn.execute("SELECT * FROM event WHERE event_id=?", (eventid,))
        items = conn.fetchall()
        for i in items:
            print (i)
        label = input("Enter the field to be Editted: ")

        if label == 'name':
         
            try:
                name = input("Enter New Event Name: ")
                conn.execute("UPDATE event SET event_name=? WHERE event_id=?", (name, eventid,))
                db_con.commit()
                print("***______________Event Name Updated successfully____________***")
                print("***______________New Record____________***")
                conn.execute("SELECT * FROM event WHERE event_id=?", (eventid,))
                items = conn.fetchall()
                for i in items:
                    print (i)
            except:
                print("Error in updating db")
        elif label == 'start_date':
            
            date1 = input('Enter the new start date in YYYY-MM-DD format: ')
            try:
                year, month, day = map(int, date1.split('-'))
                start = datetime.date(year, month, day)#edits

                try:
                	if start >= datetime.date.today():
	                    conn.execute("UPDATE event SET start_date=? WHERE event_id=?", (start, eventid,))
	                    db_con.commit()
	                    print ("***_______________Start Date Updated successfully____________***")
	                    print("***______________New Record____________***")
	                    conn.execute("SELECT * FROM event WHERE event_id=?", (eventid,))
	                    items = conn.fetchall()
	                    for i in items:
	                        print (i)
                except Exception as e:
                    print ("Error in updating Event Start Time. End Date should be Greater or Equal to Today's Date.")
            except ValueError:
                print("Invalid Input.Try Again")
                return edit_event()

        elif label == 'end_date':
            
            date2 = input('Enter the new End date in YYYY-MM-DD format: ')
            year, month, day = map(int, date2.split('-'))
            end = datetime.date(year, month, day)

            try:
                if end >= datetime.date.today():
                    conn.execute(
                        "UPDATE event SET end_date=? WHERE event_id=?", (end, eventid,))
                    db_con.commit()
                    print("\n***_____________End Date Updated successfully____________***\n")
                    print("\n***______________New Record____________***\n")
                    conn.execute("SELECT * FROM event WHERE event_id=?", (eventid,))
                    items = conn.fetchall()
                    for i in items:
                        print (i)
            except Exception as e:
                print("Error in updating End Date. End Date should be Greater or Equal to Today's Date" + str(e))

        elif label == 'venue':
            
            if type(label) is not str:
                print("Invalid Input. Input should be a number")
                return event_id
            else:
                venue = str(input("Enter the new name: "))
                try:
                    conn.execute(
                        "UPDATE event SET venue=? WHERE event_id=?", (venue, eventid,))
                    db_con.commit()
                    print("\n***______________Venue Updated successfully____________***\n")
                    print("\n***______________New Record____________***\n")
                    conn.execute("SELECT * FROM event WHERE event_id=?", (eventid,))
                    items = conn.fetchall()
                    for i in items:
                        print (i)
                except Exception as e:
                    print("Error in updating db "+ str(e))
        else:
            print("Invalid Input")
            return edit_event()
    except ValueError:
        print ("Invalid Input.Try Again")
        return edit_event()

#generate Tickets


#Ticket Validation
def ticket_validation():
    try:
        t_id =int(input ("Enter Your Ticket ID: "))
        conn.execute("SELECT * FROM tickets WHERE ticket_id=?", (t_id,))
        items = conn.fetchall()
        for row in items:
            print(row)
        print("...This Ticket is valid...")
        
    # Catch Value Error when the user inputs a wrong value
    except ValueError:
        print("Invalid Input")
        return ticket_validation()
#Generating Tickets and sendingi Emails containg the Ticket details
def generate_ticket():
    conn.execute("CREATE TABLE IF NOT EXISTS tickets( \
                    ticket_id INTEGER PRIMARY KEY, event_id INTEGER, owner_fname TEXT, owner_lname TEXT, owner_email TEXT, event_name TEXT, start_date DATE, end_date DATE, venue TEXT, FOREIGN KEY (event_id) REFERENCES event(event_id)) ")

    print ("Generate Tickets")
    print ("")

    e_id = input ("Enter Event ID: ")
    owner_fname = input ("Enter Your First Name: ")
    owner_lname = input ("Enter Your Last Name: ")
    receivers = input ("Enter your Email: ")
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    s = receivers
    if re.search(regex, s):
        match = re.search(regex, s)
        #runs if email is in correct format
        try:
        # run sql command and commit data to db
            item = conn.execute("SELECT event_name, start_date, end_date, venue FROM event WHERE event_id=?",(e_id))
            for column in item:
                name = column [0]
                s_date = column [1]
                e_date = column [2]
                venue = column [3]
                
                conn.execute("INSERT INTO tickets VALUES (null,?,?,?,?,?,?,?,?);",
                                (owner_fname, owner_lname, receivers, name, s_date, e_date, venue, e_id))
                db_con.commit()
                # t_id = conn.execute("SELECT ticket_id FROM tickets WHERE owner_fname=? AND owner_lname=? AND owner_email=? AND event_name=? AND start_date=? AND end_date=? AND venue=? AND event_id=?",
                # 				(owner_fname, owner_lname, receivers, name, s_date, e_date, venue, e_id))
            print("***Data saved data...........***")
            print ("***___Sending Email___***")
            #Sending Ticket to the user
            # details =conn.execute("SELECT * FROM tickets ORDER BY column DESC LIMIT 1;");
            # print(details)
            senders = "daisywndungu@gmail.com"      #Senders Email Address
            msg = MIMEMultipart()
            msg['From'] = senders
            msg['To'] = receivers
            msg['Subject'] = "Ticket Booking"
             
            body = " Name:" + owner_fname + " " + owner_lname +"\n Event Name:" + name + "\n Starts On: " + s_date + "\n Ends On: " + e_date + "\n Venue: " + venue #+ #"\n Ticket ID: " + t_id
            msg.attach(MIMEText(body, 'plain'))
            
            try: 
                server = smtplib.SMTP('smtp.gmail.com', 587)    #Call Gmail SMTP server
                server.starttls()
                server.login(senders, "daliken1995")        #Senders authentication
                message = msg.as_string()
                server.sendmail(senders, receivers, message)
                #if se
                print (".................Email sent..............................")
                server.quit()
            except:
                print ("Error: unable to send email")

        except:
            print("***Error in saving data...........***")
        pass
    else:
        print("Incorrect Email")
        return generate_ticket()
        

def main():
	while True:
		print("TICKECT BOOKING SERVICE")
		print("1. Add Events")
		print("2. View Events")
		print("3. Delete Events")
		print("4. Edit Events")
		print("5. Generate Tickets")
		print("6. Validate Tickets")
		print("0. Quit")
		x = input("Please select an option: ")
		x = int(x)
		if x == 0:
			#exit
			break
			pass
		elif x == 1:
			add_events()
			pass
		elif x == 2:
			#show all events
			view_all()
			pass
		elif x == 3:
			#Delete events from db
			delete_event()
			pass
		elif x == 4:
			#Edit Events
			edit_event()

		elif x == 5:
			#sends tickets to email
			generate_ticket()
		elif x == 6:
			#tickect invalidation
			ticket_validation()
		else:
			print("Invalid input")
if __name__ == '__main__':

	main()