#!/usr/bin/env python3
#Program to build calculator

#sTORE USER INPUT OF 2 NUMBERS AND THE OPERATOR
num1, operator, num2 = input('Enter Calculation').split()
#CONVERT STRINGS TO INT
num1 = int(num1)
num2 = int(num2)
#If + then add
if operator == "+":
	print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
	print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
	print("{} * {} = {}".format(num1, num2, num1*num2))
else:
	print("Use either + * or _ next time")
#Print result
