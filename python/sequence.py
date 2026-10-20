def maxar(arr):
    n=len(arr)
    if n==0:
        return 0
    result=[]
    i=0
    len=0
    while (i<n):
        curr=arr[i]
        j=i+1
        while (j<n and (arr[j]*curr>0)):
            curr=max(curr,arr[i])
            j+=1
        result.append(curr)
        len+=1
        i=j
    print("the sequence is:")
    for i in range (len):
        print(result[i])
    return sum(result)


a=[1,2,-3,-2,7,-1]

print("max sum of fair sequence:",maxar(a))
