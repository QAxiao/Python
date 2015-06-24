#!/usr/bin/env python
# coding: utf-8
#
# filename: guessnumber.py
 
def input(prompt, warning=""):
    while 1:
        value = raw_input(prompt)
        try:
            return int(value)
        except:
            print warning
 
 
def guess(num, times):
    for x in xrange(times):
        got = input(
            "Enter an integer: ",
            "Please enter an number, not char.")
        if got < num:
            print "it's smaller."
        elif num < got:
            print "it's larger"
        else:
            return x+1
    else:
        return 0
 
 
if __name__ == "__main__":
    usage = guess(23, 6)
    if usage:
        print "Great, you usage %d times to got the number" % usage
    else:
        print "You lost."
