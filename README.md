# Ticket-booking-service
A service for use at service stations where ticket bookings can be made

**Installation**

`$ git clone https://github.com/daisyndungu/bc-14-ticket-booking-service.git

`$ cd Ticket-booking-service`
 
 Create and activate a virtual environment.
 
 ```
 $ virtualenv .env
 $ source .env/bin/activate
 ```
 
 Install dependencies
 
 `$ pip install -r requirements.txt`




 **Run the app**
 
 ```

 python interface.py

 ```

 **Commands**
 
 ```
    events 411 add_events <event_name>
    events 411 view_all <table_name>
    events 411 delete_event <eventid>
    events 411 edit_event <event_id>
    events 411 ticket_invalidation <ticket_id> 

```
 
