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
coins=1
gen_password = generatepassword()
inventory =[]

def coinadd():
      while True:
	coins +=1
	time.sleep(1)
	print "you have", coins,"coins"
	time.wait(10)

def game():
    print "Welcome",user.username,"Welcome to buy and sell game"
    print "Currently you have",coins,"coins"
    if coins == 0:
      print "Well Welcome then new player, the game is very easy"
      print "Well, every second you play this game, you'll get 1 coin, n33t no? well, it is, but wait therr is more, by the journey and time pass you'll be encountred with events, such as monsters to slay, a convoy to steal from, a mission, or just a passing by merchant to offer you goodies to buy, great isnt it? well lets start"
    else:
      print "Ohh welcome back!",user.username,"want to continue you're play? >>"
      choose = raw_input('')
      if choose == "yes" or "Yes":
        coinadd()

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
