#!/usr/bin/env python
#-*- conding:utf-8 -*-
#Filename guess.py

true_num=88
i=1

print '*'*80
guess_num=int(raw_input("\nInput the number:"))
while guess_num!=true_num:
    if guess_num>true_num:
        print "It's too big!"
        guess_num=int(raw_input("\nInput the number:"))
        i+=1
        continue
    else:
        print "It's too small!"
        guess_num=int(raw_input("\nInput the number:"))
        i+=1
        continue
        
print "Amazing! you get it!"
print "You spent %d times to guess the correct number!"%i
print "Game will exit:)"
print '*'*80
