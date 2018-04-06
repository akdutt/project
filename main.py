import sys
import s_status
from spy_details import Spy
import s_friend
print("Welcome to SpyChat Application")

# Module 1: Creating Profile
# Now we have two options :-
# 1. Creating spy profile from default values.
# 2. Creating spy profile by taking input from the user.
print("Let's first create your profile\n")
profile_choice = raw_input("Do you want to continue with the current settings? (y/n) ")

if profile_choice.upper() == 'Y':
	spy = Spy("JBond", "Mr.", 25, 4.8)
else :

	#validating name
	name = raw_input("What is your name? ")
	if name.isalpha() == False and name.isspace() !=False:
		print("\nGiven name is invalid.\nTerminating application")
		sys.exit(0)

	salutation = raw_input("What should we call you? (Mr./ Mrs.) ")
	if salutation !='Mr.' and salutation !='Mrs.':
		print("invalid salutation")
		sys.exit(0)

	#validating age
	age = int(raw_input("What is your Age? "))
	if age <= 12 or age >= 50:
		print("\nGiven age is invalid.\nTerminating application")
		sys.exit(0)

	rating = float(raw_input("Plz Enter ur rating. "))
	if rating > 4 and rating <= 5:
		print("You are 3 star spy")
	elif rating > 3 and rating < 4:
		print("You are 2 star spy")
	elif rating > 2 and rating < 3:
		print("You are 1 star spy")

	else:
		print("You are 0 star spy")

	spy = Spy(name, salutation, age, rating)

# Printing spy details
print("\nHello %s %s " %(spy.salutation, spy.name))
print("We have successfully created your account")



# Module 2: Creating menu for choice
def start_chat():
	show_menu = True
	while show_menu:
		print("\nYou can select one from these operations")
		print("1. Add Friend\n2. Add Status\n3. Send Message\n4. Read Message\n5. Close application")
		menu_choice = int(raw_input("What do you want to do: "))

		if menu_choice == 1:
			print("\nYou have chosen to add a friend")
			s_friend.add_friend()
		elif menu_choice == 2:
			print("\nYou have chosen to add a status")
			spy.current_status_message = s_status.add_status(spy.current_status_message)
		elif menu_choice == 3:
			print("\nYou have chosen to send message")
			s_friend.send_message()
		elif menu_choice == 4:
			print("\nYou have chosen to read message")
			s_friend.read_message()
		elif menu_choice == 5:
			print("\nYou have chosen to close the application")
			show_menu = False
		else:
			print("\nIncorrect choice")

s_friend.load_friends()
spy.current_status_message = s_status.load_status()
start_chat()
s_friend.save_friends()
s_status.save_status()
