def shel():
	while True:
		print("Skills Map App")
		print("1. Add skill")
		print("2. Show studied skills")
		print("3. Show not studied skills")
		print("4. View learning progress")
		print("0. Quit")
		x = input("Please select an option: ")
		x = int(x)
		if x == 0:
			#exit
			break
			pass
		elif x == 1:
			add_event()
			pass
		elif x == 2:
			#show all events
			view_events()
			pass
		elif x == 3:
			#Delete events from db
			delete_event()
			pass
		elif x == 3:
			#Edit Events
			edit_event()

		elif x == 4:
			#sends tickets to email
			generate_ticket()
		elif x == 5:
			#tickect invalidation
			validate_ticket()
		else:
			print("Invalid input")