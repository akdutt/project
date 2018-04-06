import sys
import csv
from spy_details import Spy, chatMessage
import time

friends = []

def add_friend():
	print("Enter your details")
	#validating name
	friend_name = raw_input("What is your friend's name? ")
	if friend_name.isalpha() == False and friend_name.isspace() !=False:
		print("\nGiven name is invalid.\nTerminating application")
		sys.exit(0)

	friend_salutation = raw_input("Salutation? (Mr./ Mrs.) ")
	if friend_salutation !='Mr.' and friend_salutation !='Mrs.':
		print("invalid salutation")
		sys.exit(0)

	#validating age
	friend_age = int(input("Age? "))
	if friend_age <= 12 or friend_age >= 50:
		print("\nGiven age is invalid.\nTerminating application")
		sys.exit(0)

	friend_rating = float(input("friend_rating (0 to 5)"))
	if friend_rating > 4 and friend_rating < 5:
		print("You are a 3 star spy")
	elif friend_rating > 3 and friend_rating < 4:
		print("You are a 2 star spy")
	elif friend_rating > 2 and friend_rating < 3:
		print("You are a 1 star spy")

	else:
		print("u are a 0 star spy")

	new_friend = Spy(friend_name, friend_salutation, friend_age, friend_rating)
	friends.append(new_friend)

	print("Updated list of your friends")
	counter = 0
	for f in friends:
		counter += 1
		print('%d. %s' % (counter, f.name))

def select_friend():

	#Printing all the friends
	counter = 0
	for f in friends:
		counter += 1
		print('%d. %s' % (counter, f.name))

	#Asking the user to select a friend
	friend_choice = int(input("Choose from your friends: "))
	friend_choice -= 1

	#Returning the index of selected friend
	return friend_choice

def send_message():
	print("Choose the friend to whom you want to send the message")
	friend_choice = select_friend()
	message=[]
	message1 = raw_input("Enter the message to be send: ")
	formatted_time=time.asctime( time.localtime(time.time()) )
	message.append(message1)
	message.append(formatted_time)
	new_chat_message = chatMessage(message, True)

	friends[friend_choice].chats.append(new_chat_message)
	print("Your message has been sent to %s" %friends[friend_choice].name)

def read_message():
	print("Choose the friend whose message you want to read")
	sender = select_friend()

	if len(friends[sender].chats) == 0:
		print("You have no conversation with %s" %friends[sender].name)
	else:
		for i in range(len(friends[sender].chats)):
			print(friends[sender].chats[i].message)


def load_friends():
	read_object = open("friends.csv", 'r')
	reader = csv.reader(read_object)
	for row in reader:
		# order will be (name, salutation, age, friend_rating)
		name = row[0]
		salutation = row[1]
		age = int(row[2])
		friend_rating = float(row[3])
		is_online = bool(row[4])
		new_friend = Spy(name, salutation, age, friend_rating)
		friends.append(new_friend)
	read_object.close()

def save_friends():
	write_object = open("friends.csv", 'w')
	writer = csv.writer(write_object)
	for i in range(len(friends)):
		name = friends[i].name
		salutation = friends[i].salutation
		age = friends[i].age
		rating = friends[i].rating
		is_online = friends[i].is_online
		writer.writerow([name,salutation,age,rating,is_online])
	write_object.close()
