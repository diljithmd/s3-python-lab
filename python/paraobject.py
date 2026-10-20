class person:
	def __init__(self,fname,lname):
		self.firstname=fname
		self.lastname=lname
	def printname(self):
		print(self.firstname,self.lastname)
x=person("john","doe")
x.printname()
class student(person):
	def __init__(self,fname,lname,year):
		super().__init__(fname,lname)
		self.graduationyear=year
	def printyear(self):
		print(self.graduationyear)

		#person.__init__(self,fname,lname)
	#pass 
	
p=student("abinav","krishna",2028)
p.printname()
p.printyear()
