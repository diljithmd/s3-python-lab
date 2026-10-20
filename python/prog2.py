import re
x=input("enter the numner")
if(re.search(r"[a-z]",x)):
    if(re.search(r"[A-Z]",x)):
        if(re.search(r"[0-9]",x)):
            if(re.search(r"\w",x)):
                if len(x)>=8:
                    print("password is valid")
else:
    print("invlid")