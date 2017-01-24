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
                    start_date DATE, end_date DATE, description TEXT, \
                    no_of_tickets INTEGER, status TEXT ) ")
    
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
    description = input('Enter desc: ')
#Number of tickets Available
    no_of_tickets = input('Number of Tickets: ')
#Status of the event
    status = input ('Status (Open/Closed): ')
    
    try:
    #run sql command and commit data to db
    	conn.execute("INSERT INTO events VALUES (null,?,?,?,?,?,?);",\
                 (event_name, start, end, description, no_of_tickets, status ))
    	db_con.commit()
    	print ("***Data saved data...........***")
    except:
    	print ("***Error in saving data...........***")


def view_all():
	# print ("All Events (Open and Closed)")
    conn.execute("SELECT * FROM events")
    items = conn.fetchall()
    for row in items:
        print(row)

if __name__ == '__main__':

	view_all()