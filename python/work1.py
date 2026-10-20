import re
x=input("enter the password:")
if re.search(r"[a-z]",x):
    if re.search(r"[A-Z]",x):
        if re.search(r"[0-9]",x):
            if(re.search(r"\w",x)):
                if len(x)>=8:
                    print("suss")
else:
    print("not")               