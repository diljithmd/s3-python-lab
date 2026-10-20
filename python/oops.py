class car():
    def __init__(self,company,year,name,color):
        self.company=company
        self.year=year
        self.name=name
        self.color=color
    def drive(self):
        n=self.year
        if n<2015:
            print("the car not drive")
        else:
            print("it is running")


m1company=input("enter company")
m1year=int(input("enter the year"))
m1name=input("enter the model no")
m1color=input("enter the color")
m1=car(m1company,m1year,m1name,m1color,)
m1.drive()