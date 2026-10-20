def value(heads,legs):
    if(legs>heads&legs%2==0):
        rabbit=(legs-(2*heads))//2
        chiken=heads-rabbit
        print("there rabbits: ",rabbit,"\nckickens are",chiken)
    else:
        print("enter the values")
h=int(input("enter the number of heads"))
l=int(input("enter the number of legs"))
value(h,l)
