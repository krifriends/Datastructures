def MergeSort(array):
    lenA= len(array)
    if lenA<2:
        return
    mid =lenA//2   
    leftArr = array[:mid]
    rightArr = array[mid:]
    print(leftArr)
    print(rightArr)
    MergeSort(leftArr)
    MergeSort(rightArr)
    Merge(leftArr,rightArr,array)

def Merge(leftArr,rightArr,A):
    i=0
    j=0
    k=0
    lenA= len(leftArr)
    lenB= len(rightArr)
    while i<lenA and j<lenB:
        if leftArr[i]<=rightArr[j]:
            A[k]=leftArr[i]
            k+=1
            i+=1
        else:
            A[k]=rightArr[j]
            k+=1
            j+=1
    while i<lenA:
        A[k]=leftArr[i]
        k+=1
        i+=1
    while j<lenB:
        A[k]=rightArr[j]
        k+=1
        j+=1
    
inArr=[6,1,4,5,3,2]
MergeSort(inArr)
print('the array after sorting is')
print(inArr)