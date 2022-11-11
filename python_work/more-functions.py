
#aSK USER TO INPUT 2 VALUES AND STORE THEM IN VARIABLES NUM1, NUM2

num1, num2 = input('Enter 2 numbers: ').split()

#Convert the strings into int
num1 = int(num1)
num2 = int(num2)

#subtract values and store in difference
difference = num1 - num2

#Add the values and store 
sum = num1 - num2

#Multiply the values and store the products
Product = num1 * num2 

#Divide and save quotient
quotient num1 / num2

#remainder 
remainder = num1 % num2

#print the results
print("{} - {} = {}".format(num1, num2, difference))
print("{} + {} = {}".format(num1, num2, sum))
print("{} * {} = {}".format(num1, num2, Product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
