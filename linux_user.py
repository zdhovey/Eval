#! /usr/bin/python

import sys
import time

print "Booting..."
print "Enter CTRL+C to exit \n\n"


def oddfunc(b):
    print "odd function initiated. ",b+1
def evenfunc(b):
    print "even function initiated. ",b+1.5
b = 0
while True:
    oddfunc(b)
    time.sleep(.5)
    evenfunc(b)
    time.sleep(.5)
    b += 1
    if(b >= 3):
        break