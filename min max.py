def find_min_max(arr,start,end):
    if start==end:
        return arr[start],arr[start]
    if end-start==1:
        if arr[start]<arr[end]:
            return arr[start],arr[end]
        else:
            return arr[end],arr[start]

    mid=(start+end)//2
    min_left,max_left=find_min_max(arr, start, mid)
    min_right,max_right=find_min_max(arr, mid+1, end)
    min_val=min(min_left,min_right)
    max_val=max(max_left,max_right)
    return min_val,max_val

n=int(input("Enter the number of elements "))
arr=[]
for i in range(n):
    num=int(input(f"Enter the number{i+1}: "))
    arr.append(num)
min_val,max_val=find_min_max(arr,0,n-1)

print(f"minimum value: {min_val} ")
print(f"The maximum value: {max_val} ")