#code for friend

friends = [] #list
import sys


def add_friend():
	new_friend = {
		'name' : "",
		'age' : 0,
		'rating' : 0.0,
		'is_online': True
	}
	new_friend['name'] = raw_input("Enter your name: ")
	new_friend['age'] = int(input("What is your age?: "))
	new_friend['rating'] = float(input("Enter your rating (0-5): "))

	if new_friend['name'].isalpha() == False: #validating Name
		print("Plz Enter a valid Name ")
		sys.exit(0)

	if new_friend['age'] <= 12 or new_friend['age'] >= 50: #validating age
		print("Invalid age. \nAge must be b/w 12 to 50 ")
		sys.exit(0)

	friends.append(new_friend)
