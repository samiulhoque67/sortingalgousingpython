n=int(input("enter size of array :"))
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)
for i in range(0,n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(0,n):
    print(arr[i],end=" ")

