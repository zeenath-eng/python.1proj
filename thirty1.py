def selection(arr1):
    n = len(arr1)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr1[j]< arr1[mini]:
                mini=j
                arr1[i],arr1[mini]=arr1[mini],arr1[i]

arr1=[80,34,26,87,90,38]
selection(arr1)
print("sorted array is:" ,  arr1)