nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def even(x):
    return x%2==0
evens=list(filter(even,nums))
print("evens :",evens)
def odd(x):
    return x%2==1
odds=list(filter(odd,nums))
print("odds :",odds)

#lamda
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evens=list(filter(lambda x:x%2==0,nums))
print("evens :",evens)

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odds=list(filter(lambda x:x%2!=0,nums))
print("evens :",odds)