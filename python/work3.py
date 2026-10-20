import re

x=input("enter the no:")
if re.search(r"^[9,8,7]\d{9}$",x):
    print("suss")
else:
    print("no suss")