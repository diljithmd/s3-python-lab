class student():
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def printdef(self):
        print(self.fname,self.lname,self.age)

class cpp():
    def __init__(self,cpsm):
        self.threem=cpp
    def printm(self):
        print(self.threem)
fname=input("enter the first name")
lname=input("enter the last name")
age=int(input("enter the age"))
cpsm=int(input("enter the cd mark"))
x=student(fname,lname,age)
x.printdef()
#x=student(fname,lname,age,cpsm)

x.printm()
