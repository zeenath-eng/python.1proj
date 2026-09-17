#Dictionary Comprehension
dict ={}
for i in range(30):
    if i%2==0:
        dict[i]=i*i
print(dict)

dict={i:i*i for i in range(30) if i%2==0}
print(dict)