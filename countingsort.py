n=int(input("enter size of array :"))
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)

max_member=max(arr)
m2=max_member+1
arr2=[0]*m2
for i in range(0,n):
    
    arr2[arr[i]]+=1

for i in range(1,m2):
    arr2[i]=arr2[i]+arr2[i-1]

arr3=[0]*n
for i in range(n-1,-1,-1):
    arr3[arr2[arr[i]]-1]=arr[i]
    arr2[arr[i]]-=1
for i in range(0,n):
    print(arr3[i],end=" ")
    

    
    
