#! /usr/bin/python

import sys
import time
import math

print "initiating program...\n"

def foo(x):
	return math.log1p(x)

i = 0
while True:
	i += 1
	print "the natural log ",i+1," is: ",foo(i+1),"\n"
	time.sleep(0.5)
	if(i>=4):
		break
	