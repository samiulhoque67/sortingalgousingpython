def merge(arr,low,mid,high):
    n1=mid-low+1
    n2=high-mid
    larr=[0]*n1
    rarr=[0]*n2
    for i in range(0,n1):
        larr[i]=arr[low+i]
    for j in range(0,n2):
        rarr[j]=arr[mid+j+1]
    i=0
    j=0
    k=low
    
    while (i<n1 and j<n2):
        if larr[i] <=rarr[j] :
            arr[k] =larr[i];
            i+=1;
        
        else:
            arr[k]=rarr[j]
            j+=1
        
        k+=1
    
    while (i<n1):
        arr[k]=larr[i]
        i+=1
        k+=1
     
    while (j<n2):
        arr[k]=rarr[j]
        j+=1;
        k+=1;
    
    
def mergesort(arr,lo,high):
    if lo>=high:
        return
    mid=(lo+high)//2
 
    mergesort(arr,lo,mid)
    mergesort(arr,mid+1,high)
    merge(arr,lo,mid,high)

n=int(input("enter size of array :"))
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)

mergesort(arr,0,n-1)

for i in range(0,n):
    print(arr[i],end=" ")
