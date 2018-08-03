#! /usr/bin/python

import sys
import math
import time


def foo(x):
    return math.log1p(x)

num1 = input("Enter first number: \n")
num2 = input("Enter second number: \n")

print "Adding ",num1," and ",num2," equals: ",num1+num2,"\n"
time.sleep(1)
print "Subtracting ",num1," and ",num2," equals: ",num1-num2,"\n"
time.sleep(1)
print "Multiplying ",num1," and ",num2," equals: ",num1*num2,"\n"
time.sleep(1)
print "Dividing ",num1," by ",num2," equals: ",num1/float(num2),"\n"
time.sleep(1)
print "The natural log of ",num1," is ",foo(num1),"\n"
time.sleep(1)
print "The sqiare of ",num1," is ",num1*num1

