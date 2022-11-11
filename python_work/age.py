#!/usr/bin/env python3

#Different output based on age

#1 to 18 important
#21 to 50 important
#all others not important

#call age
age = eval(input("Enter age: "))

if (age >= 1) and (age <= 18):
	print("Birthday Important")
elif (age == 21) and (age == 50):
	print("Birthday Important")
elif not (age < 65):
	print("Birthday Important")
else:
	print("not important")
