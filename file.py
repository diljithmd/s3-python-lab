import pickle
import os
def addr():                  
    with open("book.dat","ab")as f:
        try:
            n=int(input("enter book no:"))
            b=input("enter book name:")
            a=input("enter authoe name:")
            p=float(input("enter price"))
            l=[n,b,a,p]  
            pickle.dump(l,f)
        except ValueError:
            print("invalid input")


def display():
        try:
            with open("book.dat","rb")as f:
                print("book details")
                while True:
                    y=pickle.load(f)
                    print(f"bookno{y[0]}|name:{y[1]}|author:{y[2]}|price:{y[3]}")
        except EOFError:
            print("end of records")
        except FileNotFoundError:
            print("file not found")

def bauthor():
    author=input("enter the auther")
    found=False
    try:
        with open("book.dat","rb")as f:
            while True:
                y=pickle.load(f)
                if y[2].lower()==author.lower():
                    print(f"found:{y[1]}|price:{y[3]}")
                    found=True
    except EOFError:
        if not found:
            print("no author found")
    except FileNotFoundError:
        print("file not found")



                




























addr()
display()
bauthor()