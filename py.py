import time

class Name:
    def __init__(self, name):
        self.name = name

coins=0

def game():
    print "Welcome",x.name,"Welcome to buy and sell game"
    print "Currently you have",coins,"coins"

x = Name(raw_input("Put here Your\'re name please: "))

if x.name == "Udi":
    print "Welcome", x.name, "You have logged in\n"
    time.sleep(2)
    print "Would you like to play a game? Yes/No: "
    press = raw_input("")
    if press == "Yes":
        print "Horray!"
        game()
    else:
        print "Ohh.. i see, see you next time!\n"

else:
    print "User",x.name,"is not registred.."
