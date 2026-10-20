from abc import ABC,abstractmethod
class shape(ABC):
	@abstractmethod
	def area(self):
		pass
	@abstractmethod
	def perimeter(self):
		pass
#x=shape()
class rectangle(shape):
	def __init__(self,length,height):
	#def __init__(self,height):
		self.length=length
		self.height=height
	def area(self):
		print(self.length*self.height)
	def perimeter(self):
		print(2*(self.length+self.height))
x=rectangle(3,5)
x.area()
x.perimeter()
