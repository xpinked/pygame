#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
import string
from random import randint

#All user information and stats
class Character:
    def __init__(self):
        self.username = ''
        self.health = 1
        self.health_max = 1

    def do_damage(self, enemies):
        damage = min(max(randint(0, self.health) - randint(0, enemies.health), 0),enemies.health)
        enemies.health = enemies.health - damage
        if damage == 0:
            print "The {} evaded the attack., try again, better this time.. k?".format(enemies.name)
        else:
            print "Take that!! **&^"
            print " Enemies health is {}".format(enemies.health)
        return enemies.health <= 0


class Enemies(Character):
    ##Enemies:
    e_names = [
    'Goblin','Slime',
    'Barbarian', 'Cocroach',
    'Dulalhan']

    def __init__(self, player):
        Character.__init__()
        self.name = self.stats(self.e_names[randint(0,4)])
        self.health = ''

    def stats(self, name):
        if self.name == self.e_names[0]:
            self.health = 60
        elif self.name == self.e_names[1]:
            self.health = 80
        elif name == self.e_names[2]:
            self.health = 100
        elif name == self.e_names[3]:
            self.health = 120
        elif name == self.e_names[4]:
            self.health = 140
        return self.health


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.state = 'refreshed'
        self.health = 100
        self.health_max = 100

#Commands Functions
    def leavegame(self):
        print " %s Baka.. Why are you leaving? hard huh...?" % self.username
        self.health = 0

    def help(self):
        print Commands.keys()

    def status(self):
        print "%s's health: %d/%d" % (self.username, self.health, self.health_max)

    def tired(self):
        print "%s You're feeling tired, you should rest.." % self.username
        self.health = max(1, self.health - 1)

    def rest(self):
        if self.state != 'refreshed':
            print "%s can't rest now!" % self.username
            self.enemies_attacks()
        else:
            print "%s Drinks a coke, and relaxes.." % self.username
            print "It is so good to rest, num num, cookies, num num!"
            time.sleep(4)
        if randint(0, 1):
            self.enemies = Enemies(self)
            print "You're been awaken by that stupid %s!" % (self.enemies.name)
            self.state = 'fight'
            self.enemies_attacks()
        else:
            if self.health < self.health_max:
                self.health = self.health + 1
            else:
                print "%s Stop sleeping so much! explore the world..." % self.username
                self.health = self.health - 1

    def explore(self):
        if self.state != 'refreshed':
            print "%s Common... you're in a middle of a fight!! attack or run! &^#@!*" % self.username
            self.enemies_attacks()
        else:
            print "%s explores a twisty passage." % self.username
            if randint(0, 1):
                self.enemies = Enemies(self)
                print "%s encounters %s!" % (self.username, self.enemies.name)
                self.state = 'fight'
            else:
                if randint(0, 1):
                    self.tired()

    def flee(self):
        if self.state != 'fight':
            print "%s runs in circles for a while." % self.username
            self.tired()
        else:
            if randint(1, self.health + 5) > randint(1, self.enemies.health):
                print "%s flees from %s." % (self.username, self.enemies.name)
                self.enemies = None
                self.state = 'refreshed'
            else:
                print "%s couldn't escape from %s!" % (self.username, self.enemies.name)
                self.enemies_attacks()

    def attack(self):
        if self.state != 'fight':
            print "%s swats the air, without notable results." % self.username
            self.tired()
        else:
            if self.do_damage(self.enemies):
                print "{} executes {}!".format(self.username, self.enemies.name)
                self.enemies = None
                self.state = 'refreshed'
                if randint(0, self.health) < 10:
                    self.health = self.health + 1
                    self.health_max = self.health_max + 1
                    print "%s feels stronger!" % self.username
                else:
                    self.enemies_attacks()

    def enemies_attacks(self):
         if self.do_damage(self):
             print "Ohh boy... The %s won, he killed you!!!!" % (self.enemies.name)

#generate password for later user
def generatepassword():
    char_set = string.ascii_lowercase + string.digits
    a = ''.join(random.sample(char_set*9, 9))
    return a



#All important variables
coins=1
gen_password = generatepassword()
inventory =[

]

#Coin adding system
#loop = trollius.get_event_loop()
def coinadd():
    while True:
          global coins
          coins +=1
          time.sleep(1)
          return coins
    #loop.stop()

#Player Commands
Commands = {
  'leavegame': Player.leavegame,
  'commands': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'run': Player.flee,
  'stab': Player.attack,
  }



def journey():
    while user.health > 0 :
        line = raw_input("> ")
        args = line.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    Commands[c](user)
                    commandFound = True
                    break
            if not commandFound:
                print "%s doesn't understand the suggestion." % user.username


def game():
    print "Welcome",user.username,"Welcome to buy and sell game"
    print "Currently you have",coins,"coins"
    if coins == 0:
      print "Well Welcome then new player, the game is very easy"
      print """
            Well, every second you play this game, you'll get 1 coin, n33t no?
            well, it is, but wait therr is more, by the journey and time pass you'll be encountred with events,
            such as monsters to slay,
            a convoy to steal from,
            a mission, or just a passing by merchant to offer you goodies to buy, great isnt it?
            well lets start
            """
    else:
      print "Ohh welcome back!",user.username,"want to continue you're play? >>"
      choose = raw_input('')
      if choose.lower() == "yes":
          print "Horray!"
          print "%s lets continue our journey shall we?" % (user.username)
          #loop.call_soon(coinadd, loop)
          #loop.run_forever()
          #loop.close()
          journey()

def beforestart():
    global username
    if user.username == "Udi":
        print "Welcome", user.username, "You have logged in\n"
        time.sleep(2)
        print "Would you like to play a game? Yes/No: "
        press = raw_input("")
        if press.lower() == "yes":
            print "Horray!"
            game()
        else:
            print "Ohh.. i see, see you next time!\n"
    else:
        print "User",user.username,"is not registred.."

if __name__ == '__main__':
    user = Player()
    user.username = (raw_input("Put here Your\'re name please: "))
    print "Hey there",user.username,"Here is you're password: ",gen_password
    print "Keep this password in hand"
    time.sleep(3)
    print "Very well..."
    time.sleep(3)
    print "Logging you in..."
    time.sleep(3)
    beforestart()