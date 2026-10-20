class math:
	def __init__(self):
		self.x=0
		self.y=0
		self.z=0


	def add(self):
		self.z=self.y+self.x
		print(self.z)


m1=math()
m1.x=int(input("enteer the number"))
m1.y=int(input("enter the other number"))
m1.add()
		
