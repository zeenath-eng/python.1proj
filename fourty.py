marks=[10,20,30,40,50,60,70,80,90,100]
new_marks=[]
for x in marks :
    new_marks.append(x+3)
print(new_marks)

#Comprehension Method
marks=[10,20,30,40,50,60,70,80,90,100]
new_marks=[x+5 for x in marks]
print(new_marks)

cubes=[]
for x in range (20):
   if x %2  ==0:
    cubes.append(x**3)
    print("using for loop:",cubes)

#Comprehension Method
easy=[x**3 for x in range(20)if x%2==0]
print("using list comprehension",easy)