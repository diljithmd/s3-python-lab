class math:
	def __init__(self,p,q):
		self.x=p
		self.y=q

	def __add__(self,other):
		x=self.x+other.x
		y=self.y+other.y
		return math(x,y)
math()
p1=math(10,20)
p2=math(45,35)
p3=p1+p2
print(p3.x,p3.y)
