#!/usr/bin/env python2.6


class Student(object):
	def __init__(self,fname,sname):
		self.fname = fname
		self.sname = sname
		self.grades = {}
		self.attend = {}
	
	def addGrade(self,subject,grade):
		if subject in self.grades.keys():
			self.grades[subject].append(grade)
		else:
			self.grades[subject] = [grade]
	
	def addAtt(self,subject,att):
		if att>1: att = 1
		if subject in self.attend.keys(): self.attend[subject].append(att)
		else: self.attend[subject] = [att]
	
	def getScore(self,subject):
		if subject in self.grades.keys():
			print sum(self.grades[subject])/float(len(self.grades[subject]))
		else:
			print "Brak przedmoitu"
			
	def getTotScore(self):
		s = [sum(i) for i in self.grades.values()]
		l = [len(i) for i in self.grades.values()]
		print '%.2f' % float(sum(s)/float(sum(l)))
		
	def getAtt(self):
		s = [sum(i) for i in self.attend.values()]
		l = [len(i) for i in self.attend.values()]
		attend  = float(sum(s)/float(sum(l))) * 100
		print '%d%%' % attend
		
stu = Student('Lukasz','Bielak')
stu.addGrade('Math',4)
stu.addGrade('Math',4)
stu.addGrade('Math',5)
stu.addGrade('Inf',4)
stu.addGrade('Inf',5)
stu.addGrade('Phy',4)
stu.addGrade('Glo',3)
stu.getScore('Math')
stu.addAtt('Glo',3)
stu.addAtt('Glo',0)
stu.addAtt('Glo',1)
stu.addAtt('Math',3)
stu.addAtt('Math',0)
stu.getTotScore()
stu.getAtt()
		
if __name__ == '__main__':
        print("Program Glowny")
else:
        print("Importowano")




