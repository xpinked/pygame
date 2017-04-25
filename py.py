#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
import string
from random import randint

#Inventory Checking
def check_inventory():
    global inventory
    damage = ''
    if 'sword' in inventory:
        damage = randint(5,25)
    elif 'wand' in inventory:
        damage = randint(10,32)
    elif 'gun' in inventory:
        damage = randint(20,45)
    return damage

#All user information and stats
class Character:
    def __init__(self):
        self.username = ''
        self.health = 1
        self.health_max = 1
        self.ename = ''

    def do_damage(self, Enemies):
        c_invent = check_inventory()
        Enemies.health = Enemies.health - c_invent
        if c_invent > 0:
            print "Take that!! **& {} You bastard ".format(char.ename)
            time.sleep(2)
            print "{} been hitted {}".format(char.ename, c_invent)
            print " Enemies health is {}".format(Enemies.health)
        else:
            print "The {} evaded the attack., try again, better this time.. k?".format(char.ename)
        return Enemies.health


class Enemies(Character):
    def __init__(self):
        Character.__init__(self)
        self.health = ''

class Player(Character, Enemies):
    def __init__(self):
        Character.__init__(self)
        self.state = 'refreshed'
        self.health = 100
        self.health_max = 100

#Commands Functions
    def my_inventory(self):
        print inventory

    def leavegame(self):
        print " {} Baka.. Why are you leaving? hard huh...?".format(self.username)
        self.health = 0

    def help(self):
        print Commands.keys()

    def status(self):
        if Enemies.health > 0:
            print "{}'s health: {}{}".format(self.username, self.health, self.health_max)
            print "{} health: {}".format(self.ename, Enemies.health)
            print "{}'s state: {}".format(self.username, self.state)
        else:
            print "{}'s health: {}{}".format(self.username, self.health, self.health_max)
            print "{}'s state: {}".format(self.username, self.state)

    def tired(self):
        print "%s You're feeling tired, you should rest.." % self.username
        self.health = max(1, self.health - 1)

    def rest(self):
        if self.state != 'refreshed':
            print "%s can't rest now!" % self.username
            self.Enemies_attacks()
        else:
            print "%s Drinks a coke, and relaxes.." % self.username
            print "It is so good to rest, num num, cookies, num num!"
            time.sleep(4)
        if randint(0, 1):
            print "You're been awaken by that stupid {}!".format(self.ename)
            self.state = 'fight'
            self.Enemies_attacks()
        else:
            if self.health < self.health_max:
                self.health = self.health + 1
            else:
                print "%s Stop sleeping so much! explore the world..." % self.username
                self.health = self.health - 1

    def explore(self):
        if self.state != 'refreshed':
            print "%s Common... you're in a middle of a fight!! attack or run! &^#@!*" % self.username
            self.Enemies_attacks()
        else:
            print "%s explores a twisty passage." % self.username
            if randint(0, 3):
                print "%s encounters %s!" % (self.username, self.ename)
                self.state = 'fight'
            else:
                if randint(0, 6):
                    self.tired()

    def flee(self):
        if self.state != 'fight':
            print "%s runs in circles for a while." % self.username
            self.tired()
        else:
            if randint(1, self.health + 5) > randint(1, Enemies.health):
                print "%s flees from %s." % (self.username, self.ename)
                self.state = 'refreshed'
            else:
                print "%s couldn't escape from %s!" % (self.username, self.ename)
                self.Enemies_attacks()

    def attack(self):
        if self.state != 'fight':
            print "%s swats the air, without notable results." % self.username
            self.tired()
        else:
            if self.do_damage(Enemies):
                print "{} executes {}!".format(self.username, self.ename)
                self.state = 'refreshed'
                if randint(0, self.health) < 10:
                    self.health = self.health + 1
                    self.health_max = self.health_max + 1
                    print "%s feels stronger!" % self.username
                else:
                    self.Enemies_attacks()

    def Enemies_attacks(self):
         if self.do_damage(self)  <= 0:
             print "Ohh boy... The %s won, he killed you!!!!" % (self.ename)

##Functions for later use

#generate password for later user
def generatepassword():
    char_set = string.ascii_lowercase + string.digits
    a = ''.join(random.sample(char_set*9, 9))
    return a



#All important variables
##Enemies names:
e_names = ['Goblin','Slime','Barbarian', 'Cocroach','Dulalhan']
coins=1
gen_password = generatepassword()
inventory =['sword']
#Player Commands
Commands = {
  'leavegame': Player.leavegame,
  'commands': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'run': Player.flee,
  'stab': Player.attack,
  'inventory': Player.my_inventory
  }

#defines Enemies names
def stats(name):
    if name == e_names[0]:
        Enemies.health = 60
    elif name == e_names[1]:
        Enemies.health = 80
    elif name == e_names[2]:
        Enemies.health = 100
    elif name == e_names[3]:
        Enemies.health = 120
    elif name == e_names[4]:
        Enemies.health = 140
    return name


#Coin adding system
#loop = trollius.get_event_loop()
def coinadd():
    while True:
          global coins
          coins +=1
          time.sleep(1)
          return coins
    #loop.stop()

def journey():
    while char.health > 0 :
        line = raw_input("> ")
        args = line.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    Commands[c](char)
                    commandFound = True
                    break
            if not commandFound:
                print "%s doesn't understand the suggestion." % char.username


def game():
    print "Welcome",char.username,"Welcome to buy and sell game"
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
      print "Ohh welcome back!",char.username,"want to continue you're play? >>"
      choose = raw_input('')
      if choose.lower() == "yes":
          print "Horray!"
          print "%s lets continue our journey shall we?" % (char.username)
          #loop.call_soon(coinadd, loop)
          #loop.run_forever()
          #loop.close()
          journey()

def beforestart():
    global username
    if char.username == "Udi":
        print "Welcome", char.username, "You have logged in\n"
        time.sleep(2)
        print "Would you like to play a game? Yes/No: "
        press = raw_input("")
        if press.lower() == "yes":
            print "Horray!"
            game()
        else:
            print "Ohh.. i see, see you next time!\n"
    else:
        print "User",char.username,"is not registred.."

if __name__ == '__main__':
    char = Player()
    char.username = (raw_input("Put here Your\'re name please: "))
    char.ename = stats(e_names[randint(0,4)])
    print "Hey there",char.username,"Here is you're password: ",gen_password
    print "Keep this password in hand"
    time.sleep(3)
    print "Very well..."
    time.sleep(3)
    print "Logging you in..."
    time.sleep(3)
    beforestart()
