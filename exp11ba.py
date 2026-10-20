from abc import ABC,abstractmethod
class shape(ABC):
	@abstractmethod
	def area(self):
		pass
	@abstractmethod
	def perimeter(self):
		pass
#x=shape()
class circle(shape):
	def __init__(self,radius):
		self.radius=radius
	def area(self):
		print("area=",3.14*self.radius*self.radius)
	def perimeter(self):
		print("perimeter=",2*3.14*self.radius)
x=circle(5)
x.area()
x.perimeter()
