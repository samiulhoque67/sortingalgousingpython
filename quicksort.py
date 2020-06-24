def partition(arr,lo,high):
    pivot=arr[high]
    i=lo-1
    for j in range(lo,high+1):
        if(arr[j]<pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1



def quicksort(arr,lo,high):
    if lo>=high:
        return
    p=partition(arr,lo,high)
    quicksort(arr,lo,p-1)
    quicksort(arr,p+1,high)

n=int(input("enter size of array :"))
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)

quicksort(arr,0,n-1)

for i in range(0,n):
    print(arr[i],end=" ")
