#List Comprehension
list=[]
for i in range(30):
    if i%2==0:
      list.append(i)
print(list)

#instead of above lines
list1=[i for i in range(30) if i%2==0]
print(list)

list2=[i**2 for i in range(30) if i%2==0]
print(list)
