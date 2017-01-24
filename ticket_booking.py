import sqlite3
import datetime


#connect to database
db_con = sqlite3.connect("event_booking.db")
#create a temporary memory to store data
conn = db_con.cursor()

def add_items():
    #create table
    conn.execute("CREATE TABLE IF NOT EXISTS events( \
                    event_id INTEGER PRIMARY KEY, event_name TEXT, \
                    start_date DATE, end_date DATE, venue TEXT,) ")
    
    #get user input
    print("Enter an Event")
    print("")
    
    event_name = input('Enter Event name: ') 
#Event Start Date
    date1_entry = input('Enter date event begins in YYYY-MM-DD format: ')
    year, month, day = map(int, date1_entry.split('-'))
    start = datetime.date(year, month, day)
#Event End Date
    date2_entry = input('Enter date event ends in YYYY-MM-DD format: ')
    year, month, day = map(int, date2_entry.split('-'))
    end = datetime.date(year, month, day)
#Event Description
    venue = input('Enter Venue: ')
#Number of tickets Available
#    no_of_tickets = input('Number of Tickets: ')
#Status of the event
#   status = input ('Status (Open/Closed): ')
    
    try:
    #run sql command and commit data to db
    	conn.execute("INSERT INTO events VALUES (null,?,?,?,?);",\
                 (event_name, start, end, venue ))
    	db_con.commit()
    	print ("***Data saved data...........***")
    except:
    	print ("***Error in saving data...........***")

def view_all():
	# print ("All Events (Open and Closed)")
    conn.execute("SELECT * FROM events")
    items = conn.fetchall()
    for row in items:
    	print (row)

def delete_event():
	eventid = str(input('Please enter ID of the event to be deleted: '))
	try:

		conn.execute("DELETE FROM events WHERE event_id=?", (eventid,))
		db_con.commit()
		print ("Event with ID " + eventid + " has been deleted successfully__________***")
	except:
		print ("Error in deleting file")		


def shel():
	while True:
		print("TICKECT BOOKING SERVICE")
		print("1. Add Events")
		print("2. View Events")
		print("3. Delete Events")
		print("4. Edit Events")
		print("3. Genarate Tickets")
		print("4. Validate Tickets")
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
			validate_ticket()
		else:
			print("Invalid input")
if __name__ == '__main__':

	shel()