def binary(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]>target:
            right=mid-1
        elif arr[mid]<target:
            left=mid+1
        else :
            return mid
arr=[1,2,3,4,5,6,7,8,9]
print(arr,binary(arr,10))#None
print(arr,binary(arr,7))#6(index)
print(arr,binary(arr,3))#2(index)