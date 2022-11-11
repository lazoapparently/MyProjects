#!/usr/bin/env python3
#This program demonstrates inhertiance

class Person(object):

#constructor
	def __init__(self, name, id):
		self.name = name
		self.d = id

#To check if person is an employee
	def Display(self):
		print(self.name, self.id)

#Driver code
		emp = Person("Lazo", 547) #an object
		emp.Display()
