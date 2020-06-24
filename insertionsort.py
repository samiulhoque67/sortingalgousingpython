#insertion sort checks the previous items from it pointed.




n=int(input("enter size of array :"))
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)
    
for i in range(1,n):
    k=arr[i]
    j=i-1
    while(j>=0 and arr[j]>k):
        arr[j+1]=arr[j]
        j=j-1

    arr[j+1]=k

    
for i in range(0,n):
    print(arr[i],end=" ")

