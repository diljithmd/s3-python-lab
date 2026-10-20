import pickle
def add_record():
	f=open("book.dat","ab")
	n=int(input("Enter Book No: "))
	b=input("Enter Book Name: ")
	a=input("Enter Author Name: ")
	p=float(input("Enter Price: "))
	l=[n,a,b,p]
	pickle.dump(l,f)
	f.close()
def display_record():
	f=open("book.dat","rb")
	print("Book details: \n")
	while(1):
		try:
			y=pickle.load(f)
			print("Book No: ",y[0],"\nBook Name: ",y[1],"\nBook Author: ",y[2],"\nBook Price: ",y[3])
		except EOFError:
			print("Reached End-Of-File")
		finally:
			exit(1)
	f.close()
def book_by_author():
	f=open("book.dat","rb")
	a=int(input("enter the author's anme"))
	while(1):
		try:
			y=pickle.load(f)
			if(y[2]==a):
				print("the book is written by",a,x[1])
		except EOFError:
			print("Reached End-Of-File")
		finally:
			exit(1)
def book_by_price():
	f=open("book.dat","rb")
	a=int(input("enter the book price"))
	while(1):
		try:
			y=pickle.load(f)
			if(y[3]<=a):
				print(y[1],"|",y[3])
		except EOFError:
			print("Reached End-Of-File")
		finally:
			exit(1)
def copy_data():
	f=open("book.dat","rb")
	g=open("costly_book.dat","wb")
	a=int(input("enter the price"))
	count=0
	while(1):
		try:
			y=pickle.load(f)
			if(x[3]>a):
				l=(x[1],x[3])
				count=count+1
				pickle.dump(l,g)
		except EOFError:
			break
	f.close()
	g.close()
	f=open("costly_book.dat","wb")
	print("the book record are")
	while(1):
		try:
			y=pickle.load(f)
			print("BOOK NAME",y[0],"price:",y[2])
		except EOFError:
			break
	print("1.Insert\n2.Display\n3.Exit")
	choice=int(input("Enter your choice: "))
	if(choice==1):
		add_record()
	elif(choice==2):
		display_record()
	elif(choice==3):
		exit(1)
	else:
		print("Invalid Choice...")