import sys
import default as df
import s_friend as sf
import s_status as ss


def start_chat(spy_name, spy_age, spy_rating):
	current_status_message = None
	show_menu = True

	while show_menu == True:
		menu_choice = int(input("1. Add a status update\n2. Add a Friend\n3. Exit the application"))
		if menu_choice == 1:
			#update status
			print("You have chosen to add a status")
			current_status_message = ss.add_status(current_status_message)
			#print(current_status_message)
		elif menu_choice == 2:
			print("You have chosen to add a friend")
			sf.add_friend()
		elif menu_choice == 3:
			show_menu = False

#Welcome
print("Welcome to spychat Program")
choice = raw_input("Proceed with default settings(y/n)?: ")

spy = {
	'name' : "",
	'age' : 0,
	'rating' : 0.0,
	'is_online': True
}

if choice.upper() ==  'Y':
	spy['name'] = df.spy['name']
	spy['age'] = df.spy['age']
	spy['rating'] = df.spy['rating']
	spy['is_online'] = df.spy['is_online']
else:
	spy['name'] = raw_input("Enter your name: ")
	spy['age'] = int(input("What is your age?: "))
	spy['rating'] = float(input("What is your rating?: "))
	spy['is_online'] = True

#validation name & age
if spy['name'].isalpha() == False:
	print("Invalid name")
	sys.exit(0)

if spy['age'] <= 12 or spy['age'] >= 50:
	print("Invalid age")
	sys.exit(0)

print("hello " + spy['name'] + ".")
start_chat (spy['name'], spy['age'], spy['rating'])
