from random import*
from time import *
def quick_sort(array):
    if len(array)<=1:
        return array

    pivot=array[randint(0,len(array)-1)]
    less=[x for x in array if x<pivot]
    equal=[x for x in array if x==pivot]
    greater=[x for x in array if x>pivot ]
    return quick_sort(less)+equal+quick_sort(greater)

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
    sorted_number=quick_sort(array)
    print("Sorted value is ")
    printList(sorted_number)
    print("Time taken to sort " ,(process_time()-start_time)*1000,"ms")