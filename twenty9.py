def insertion (arr1):
    n=len(arr1)
    for i in range(1,n):
        key=arr1[i]
        f=i-1
        while f>=0 and key < arr1[f]:
            arr1[f+1]=arr1[f]
            f-=1
            arr1[f+1]=key


arr1=[90,70,60,40,10]
insertion(arr1)
print("sorted array is:", arr1)