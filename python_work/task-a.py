#!/usr/bin/env python3

#Ask for age
age = eval(input("Enter Age: "))

#looping
if age < 5:
	print("Too young for school")

#if 5
elif age == 5:
	print("Go to Kindergarten")
elif (age > 5) and (age <= 17):
	grade = age - 5
	print("Go to Grade {}" .format(grade))

else:
	print("Go to college")
