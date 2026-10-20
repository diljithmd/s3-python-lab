def age():
	age=int(input("enter the age"))
	if age<0:
		err=ValueError("{0}is not valid age",format(age))
		raise err
	else:
		print(age)
	return age
age()
