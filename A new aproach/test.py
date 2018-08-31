#!/usr/bin/python
# -*- coding: utf-8 -*-
###
#A Place to test your skills
###

def Hello(Name):
    print("Your name is {}".format(Name));

while True:
    t=raw_input("Write Here your name :> ")
    if t in ['Elad']:
        print("HAHA Baka {}, I'll never let you to use my program".format(t));
    elif t in ['Quit']:
        print("Ohh, See you later then <3");
        break
    else:
        Hello(t);
