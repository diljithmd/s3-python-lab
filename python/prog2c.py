import re
x=input("enter the no")
if re.search(r"^[789]\d{9}$",x):
    print("valid")
else:
    print("invlid")