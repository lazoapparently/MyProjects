#!/usr/bin/env python3

money = input("How much do you want to invest?: ")
interest_rate = input("Interest Rate: ")

money = float(money)

interest_rate = float(interest_rate) * .01

for i in range(10):
	money = money + (money * interest_rate)

print("Investment after 10 years : {:.2f}".format(money))
