import time
import random
import string

class Users:
    def __init__(self, username):
        self.username = username

def generatepassword():
    char_set = string.ascii_lowercase + string.digits
    a = ''.join(random.sample(char_set*9, 9))
    return a

#variables
coins=0
gen_password = generatepassword()

def game():
    print "Welcome",user.username,"Welcome to buy and sell game"
    print "Currently you have",coins,"coins"

def beforestart():
        if user.username == "Udi":
            print "Welcome", user.username, "You have logged in\n"
            time.sleep(2)
            print "Would you like to play a game? Yes/No: "
            press = raw_input("")
            if press == "Yes":
                print "Horray!"
                game()
            else:
                print "Ohh.. i see, see you next time!\n"

        else:
            print "User",user.username,"is not registred.."

user = Users(raw_input("Put here Your\'re name please: "))
print "Hey there",user.username,"Here is you're password: ",gen_password
print "Keep this password in hand"
time.sleep(3)
print "Very well..."
time.sleep(3)
print "Logging you in..."
time.sleep(3)
beforestart()
