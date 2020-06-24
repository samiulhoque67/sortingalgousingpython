# in selection sort ,at first first position will be sorted,then next position

n=int(input("enter size of array :"))
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)
for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
for i in range(0,n):
    print(arr[i],end=" ")

