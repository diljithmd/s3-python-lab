import pickle
import os

def add_reco():
   
        with open("book.dat","ab")as f:
            n=int(input("enter the no:"))
            m=input("enter the name:")
            r=input("enter the author:")
            p=float(input("enter the price:"))
            l=[n,m,r,p]
            pickle.dump(l,f)
    
            
def display():
    try:
        with open("book.dat","rb")as f:
            
            while True:
                y=pickle.load(f)
                print(f"no{y[0]}\nname{y[1]}\nauthor{y[2]},\nprice{y[3]}\n")
    except EOFError:
        print("all data print")
    except FileNotFoundError:
        print("file not found")

def cou():
    count=0
    try:
        with open ("book.dat","rb")as f:
            while True:
                try:
                    y=pickle.load(f)
                    if y[3]>500:
                        print(y)
                        count=count+1
                    print(count)   
                except EOFError:
                    
                    break
    except FileNotFoundError:
        print("not found")

def author():
    author=input("enter the author")
    found=False
    try:
          with open("book.dat","rb")as f:
               while True:
                    y=pickle.load(f)
                    if author==y[2]:
                        
                        print(f"no{y[0]}\nname{y[1]}\nauthor{y[2]},price{y[3]}")
                        found=True
    except EOFError:
        if not found:
         print("all data print")
    except FileNotFoundError:
        print("file not found")

def delete():
    bno=int(input("enter the code"))
    found=False
    try:
        with open("book.dat","rb")as f,open("temp.dat","wb")as t:
            while True:
                try:
                    y=pickle.load(f)
                    if y[0]!=bno:
                        pickle.dump(y,t)
                    else:
                        found=True
                except EOFError:
                    break
        if found:
            os.remove("book.dat")
            os.rename("temp.dat","book.dat")
            print("deletrd")
        else:
            os.remove("temp.dat")
            print("code is not found")
            
    except FileNotFoundError:
        print("file not found")

def update():
    bookno=int(input("enteer the code"))
    found=False
    try:
        with open("book.dat","rb")as f,open("temp.dat","wb")as t:
            while True:
                try:
                    y=pickle.load(f)
                    if y[0]==bookno:
                       
                        y[1]=input("enter the name")
                        y[2]=input("enter the author")
                        y[3]=int(input("enter the price"))
                    pickle.dump(y,t)
                except EOFError:
                    break
        os.remove("book.dat")
        os.rename("temp.dat","book.dat")
        if found==True:
            print("sus")
        else:
            print("not file")

    except FileNotFoundError:
        print("not file")

                    

            

add_reco()
display()
update()
display()



add_reco()

cou()

delete()
display()
author()

