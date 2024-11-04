from random import*
from time import *
def mergesort(array):
    if len(array)>1:
        m=len(array)//2
        L=array[:m]
        R = array[m:]
        mergesort(L)
        mergesort(R)
        i=j=k=0
        while i<len(L)<j<len(R):
            if L[i]<R[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j<len(R):
            array[k] = R[j]
            j += 1
            k += 1

def printList(array):
    for i in range(len(array)):
        print(array[i] ,end=" ")
    print()

if __name__=='__main__':
    start_time=process_time()
    n=int(input("Enter how many elements ?"))
    array=[]
    for j in range(n):
        array.append(randint(5000,15000))
    print(array)
    mergesort(array)
    print("Sorted value is ")
    printList(array)
    print("Time taken to sort " ,(process_time()-start_time)*1000,"ms")