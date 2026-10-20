def fairseq(a):
    l2=[]
    l3=[]
    l4=[]
    a.sort()
    a.reverse()
    for i in range(len(a)):
        if a[i]>0:
            l2.append(a[i])
        else:
            l3.append(a[i])
    if len(l2)>len(l3):
        d=len(l2)-len(l3)
        for i in range(d):
            l2.pop()
    else:
        d=len(l3)-len(l2)
        for i in range(d):
            l3.pop()
    for i in range(len(l2)):
        l4.append(l2[i])
        l4.append(l3[i])
    return l4
a=[]
print("positive and negative")
n=int(input("enter the size"))
for i in range(n):
    e=int(input("enter the no"))
    a.append(e)
print("fair seq")
result=fairseq(a)
print(result)
