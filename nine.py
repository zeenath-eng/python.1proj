x = 10
y= 10
print (x is y)
z= x 
print (z is y)
print (id (x))
print (id (y))
print (id (z))


s1 ="zeenath"
s2 = "zeenath"
print(s1 is s2)


l1 =[1,2,3]
l2 =[1,2,3]
print(l1 is l2)
print(l1==l2)
print(id (l1))
print(id(l2))

n1 =None
n2 =None
print(n1 is n2)

n1 =None
n2 =None
print(n1 is not n2)