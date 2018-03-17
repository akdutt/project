import sys
import default

choice = input("Enter 1 if you want default settings ") 
if choice == '1': #verifying choice
    spy_name = default.spy_name
    spy_salutation = default.spy_salutation
    spy_age = default.spy_age
    spy_rating = default.spy_rating
    print ("Hello " +spy_salutation + spy_name)
    print ("Your age is " + spy_age)
    print ("Your rating is" + spy_rating)
else: #takeing input form user    
     spy_name = input("Enter your name ")
     if spy_name.isalpha() == False: #cheaking weather name entered is valid or not
        print("Plz. Enter a valid name.")
        print("Name should be only in alphabets (A-Z or a-z)")
        sys.exit(0) #if name is not valid exit

     spy_salutation = input("Enter your Salutaton (Mr. or Mrs.):")

     spy_age = input("Enter your age ")
     if type(spy_age)== int: #cheaking age is valid or not
         if int(spy_age) <= 12:
             print("Age below 12 not allow")
             sys.exit(0)   
         if int(spy_age) >=50:
             print("Age is above 50 not allow")
             sys.exit(0)
     spy_rating = input("Enter your rating (A, B or c) ")
     print ("Hello  " + spy_salutation + spy_name) #printing wellcome msg
     print ("Your age is  "+ spy_age)
     print ("Your rating is " + spy_rating)

     if spy_rating == 'A':
        print("You are a 3 star spy")
     elif spy_rating == 'B':
        print("You are a 2 star spy") #compairing ratings
     elif spy_rating == 'C':
        print("You are a 1 star spy")
     else:
        print("You have entered incorrect rating")
        sys.exit(0) 
     #print ("Hello" + spy_salutation + spy_name)
     #print("Your age is " + spy_age)
     #print ("Your rating is" + spy_rating)

    
        

