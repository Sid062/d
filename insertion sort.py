array=[]
n=int(input("Enter the number of elements "))
for i in range(0,n):
    ele=int(input(f"Enter the elements{i+1} "))
    array.append(ele)
print("Elements before sorting",array)
for i in range(1,len(array)):
    key=array[i]
    j=i-1
    while j>=0 and key<array[j]:
        array[j+1]=array[j]
        j-=1
    array[j+1]=key
print("Elements after sorting : ",array)