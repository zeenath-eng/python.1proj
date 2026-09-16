def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [27, 13, 32, 20, 40]

print(linear(arr, 20))
print(linear(arr, 13))
print(linear(arr, 46))