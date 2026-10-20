def age():
	age=int(input("enter the age"))
	if(age<0):
		error=ValueError("{0} is  invalid".format(age))
		raise error
	return age
age()
