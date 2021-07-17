def QuickSort(A,start,end):
    if start<end:
        pIndex= partitionIndex(A,start,end)
        QuickSort(A,start,pIndex-1)
        QuickSort(A,pIndex+1,end)

def partitionIndex(A,start,end):
    pIndex = start
    pivot= A[end]
    for i in range(start,end):
        if A[i]<=pivot:
            temp=A[i]
            A[i]=A[pIndex]
            A[pIndex]=temp
            pIndex+=1
    temp=A[pIndex]
    A[pIndex]=A[end]
    A[end]=temp
    return pIndex

A=[1,6,4,7,9,8,3]
print(QuickSort(A,0,len(A)-1))
print(A)
