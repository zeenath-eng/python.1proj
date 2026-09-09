#break
l1 = range (10)
for i in l1:
    if (i==6):
        break
    print(i)

#continue
l1 = range (10)
for i in l1:
    if (i==6):
        continue
    print(i)

items = [1,2,3,4,5,6,7]
target = 4
for item in items: 
    if item == target:
        print("item found:",item)
        break

items = [1,2,3,4,5,6,7]
target = 4
for item in items: 
    if item == target:
        print("item found:",item)
        continue