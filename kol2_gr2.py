#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

#!/usr/bin/env python2.6

from collections import defaultdict

class Student(object):
	def __init__(self,name,sname):
		self.fname = name
		self.sname = sname
		self.score = {}
		
	
	def add_grade(self,clas,grade):
		self.score.setdefault(clas, []).append(grade)
		

class Class(object):
	def __init__(self,name):
		self.name = name
		self.Students = []
	
	def add_stud(self,Student):
		if Student not in self.Students:
			self.Student = self.Student.append(Student)

	def add_grad(self,Student,grade):
		if Student in self.Students:
			Student.add_grade(self.name,grade)

	def add_att(self,Student,grade):
		if Student in self.Students:
			Student.add_grade(self.name,grade)




