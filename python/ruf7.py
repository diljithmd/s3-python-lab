class person:
    def __init__(self):
        self.name=""
        self.age=12
        self.height=1.8
        self.weight=60
        
    def getbmi(self):
        d=self.height*self.height
        bmi=self.weight/d
        if bmi>30:
            print("obesy")
        elif bmi<18.5:
            print("under weight")
        else:
            print("healthy")
    
m1=person()


m1.name=input("enter the name")
m1.age=int(input("enter the age"))
m1.height=float(input("enter the height"))
m1.weight=float(input("enter the weight"))
m1.getbmi()



