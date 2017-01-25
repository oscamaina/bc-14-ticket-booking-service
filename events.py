import sqlite3
import datetime
import smtplib
 

# connect to database
db_con = sqlite3.connect("event_booking.db")
# create a temporary memory to store data
conn = db_con.cursor()


def add_items():
    # create table
    conn.execute("CREATE TABLE IF NOT EXISTS event( \
                    event_id INTEGER PRIMARY KEY, event_name TEXT, start_date DATE, end_date DATE, venue TEXT ) ")

    # get user input
    print("Enter an Event")
    print("")

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
# Number of tickets Available
#    no_of_tickets = input('Number of Tickets: ')
# Status of the event
#   status = input ('Status (Open/Closed): ')

    try:
        # run sql command and commit data to db
        conn.execute("INSERT INTO event VALUES (null,?,?,?,?);",
                     (event_name, start, end, venue))
        db_con.commit()
        print("***Data saved data...........***")
    except:
        print("***Error in saving data...........***")

# function to fetch all the Events in the Database


def view_all():
    try:      # print ("All Events (Open and Closed)")
        conn.execute("SELECT * FROM event")
        items = conn.fetchall()
        for row in items:
            print(row)
        # print ("Event ID = ", row[0])
        # print ("EVENT NAME = ", row[1])
        # print ("START DATE = ", row[2])
        # print ("END DATE = ", row[3])
        # print ("DESCRIPTION = ", row[4])
        # print ("NUMBER OF TICKETS = ", row[5])
        # print ("STATUS = ", row[6]), "\n"
        print ("***____________All Events Displayed Above___________***")
    except:
        print ("Error in printing")
# Function to delete Events


def delete_event():
    eventid = int(input('Please enter ID of the event to be deleted: '))
    try:

        conn.execute("DELETE FROM event WHERE event_id=?", (eventid,))
        db_con.commit()
        print("Event with ID " + eventid +
              " has been deleted successfully__________***")
    except:
        print("Error in deleting file")


def edit_event():
    # print ("Enter The Module/Attribute to be Editted beginning with the key word 'edit'")
    print(
        "Use name to edit event name, start_date to edit when the event begin, end_date to edit when the event ends and venue to edit the venue")
    print("Example: What would you like to edit?: venue ")
    label = str(input("What would you like to edit?:  "))
    # compares user input to the set conditions
    if label == 'name':
        event_id = int(input("Enter te ID of the event to be modified: "))
        if type(event_id) is not int:
            print("Invalid Input. Input should be a Number")
            return event_id

        else:
            event_name = str(input("Enter the new name: "))
            try:
                conn.execute(
                    "UPDATE event SET event_name=? WHERE event_id=?", (event_name, event_id,))
                db_con.commit()
                print(
                    "***______________Event Name Updated successfully____________***")
            except:
                print("Error in updating db")
    elif label == 'start_date':
        event_id =int (input("Enter the ID of the event to be modified: "))
        date1 = input('Enter the new start date in YYYY-MM-DD format: ')
        year, month, day = map(int, date1.split('-'))
        start = datetime.date(year, month, day)
        try:
            conn.execute("UPDATE event SET start_date=? WHERE event_id=?", (start, event_id,))
            db_con.commit()
            print ("***_______________Start Date Updated successfully____________***")
        except:
            print ("Error in updating db")

    elif label == 'end_date':
        event_id = str(input("Enter te ID of the event to be modified: "))
        date2 = input('Enter the new start date in YYYY-MM-DD format: ')
        year, month, day = map(int, date2.split('-'))
        end = datetime.date(year, month, day)
        try:
            conn.execute(
                "UPDATE event SET end_date=? WHERE event_id=?", (end, event_id,))
            db_con.commit()
            print(
                "***_____________End Date Updated successfully____________***")
        except:
            print("Error in updating db")

    elif label == 'venue':
        event_id = int(input("Enter te ID of the event to be modified: "))
        if type(event_id) is not int:
            print("Invalid Input. Input should be a number")
            return event_id
        else:
            venue = str(input("Enter the new name: "))
            try:
                conn.execute(
                    "UPDATE event SET venue=? WHERE event_id=?", (venue, event_id,))
                db_con.commit()
                print(
                    "***______________Venue Updated successfully____________***")
            except:
                print("Error in updating db")
    else:
        print("Invalid Input")
        return label


def generate_ticket():
    conn.execute("CREATE TABLE IF NOT EXISTS tickets( \
                    ticket_id INTEGER PRIMARY KEY, event_id INTEGER, owner_fname TEXT, owner_lname TEXT, owner_email TEXT, event_name TEXT, start_date DATE, end_date DATE, venue TEXT, FOREIGN KEY (event_id) REFERENCES event(event_id)) ")

    print ("Generate Tickets")
    print ("")

    event_id = input ("Enter Event ID: ")
    owner_fname = input ("Enter Your First Name: ")
    owner_lname = input ("Enter Your Last Name: ")
    receivers = input ("Enter your Email: ")
    try:
        # run sql command and commit data to db
        item = conn.execute("SELECT event_name, start_date, end_date, venue FROM event WHERE event_id=?",(event_id))
        for column in item:
            name = column [0]
            s_date = column [1]
            e_date = column [2]
            venue = column [3]
            
            conn.execute("INSERT INTO tickets VALUES (null,?,?,?,?,?,?,?,?);",
                            (owner_fname, owner_lname, receivers, name, s_date, e_date, venue, event_id))
            db_con.commit()
        print("***Data saved data...........***")
        print ("***___Sending Email___***")
        senders = "daisywndungu@gmail.com"      #Senders Email Address
        # receivers = input("Enter your email: ") #Receiver email Address
        message = """From: From Person <from@fromdomain.com>
        To: To Person <to@todomain.com>
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """
        try: 
            server = smtplib.SMTP('smtp.gmail.com', 587)    #Call Gmail SMTP server
            server.starttls()
            server.login(senders, "daliken1995")        #Senders authentication
            
            server.sendmail(senders, receivers, message)
            #if se
            print (".................Email sent..............................")
            server.quit()
        except:
            print ("Error: unable to send email")

    except:
        print("***Error in saving data...........***")
    pass

if __name__ == '__main__':

    generate_ticket()
