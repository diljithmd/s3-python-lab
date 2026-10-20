l=[5,8,2,9]
try:
	print(l)
	a=int(input("enter  index of element to the no:"))
	b=int(input("enter denominator:"))
	d=a/b
	c=int(input("enter the index:"))
	
	print(l[c])
except IndexError:
	print("index only 1-3:")
except ValueError:
	print("ivalid data entered")
except ZeroDivisionError :
	print("divisor shold not be zero")
else: 
	print("divivision result",d)
