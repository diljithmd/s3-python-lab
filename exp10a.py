class person:
	def __init__(self):
		self.name="abi"
		self.age=30
		self.height=157
		self.weight=60
	def getbmi(self):
		h=self.height
		bmi=self.weight/(h*h)
		if bmi>30:
			print("over weight")
		elif bmi<=18.5:
			print ("under weight")
		else:
			print("healthy")




m1=person()
m1.nam=input("Enter the name:")
m1.age=int(input("enter the age:"))
m1.height=float(input("Enter the height:"))
m1.weight=int(input("enter the weight:"))
m1.getbmi()
		
		
