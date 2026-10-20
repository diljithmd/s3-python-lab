class b_mi():
    def __init__(self,height,weight,name,age):
        self.height=height
        self.weight=weight
        self.name=name
        self.age=age
    def sub(self):
        h=self.height
        bmi=self.weight/(h*h)
        if bmi>24:
            print("is over")
        elif bmi<18:
            print("is under")
        else:
            print("normal")

h=float(input("enter the height"))
g=float(input("enter the weight"))
a=input("enter the name")
r=float(input("enter the age"))
person=b_mi(h,g,a,r)
person.sub()


