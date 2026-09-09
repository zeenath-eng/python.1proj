#dictionary

dict= {"name" :"zeenath", "age":20,"marks":90.99}
print(dict)
print(dict["age"])

#if ,elif &else
age =int(input("enter your age :"))
if age >=18:
    print("you can apply for licence")
else :
    print("you caanot apply")

Good ="no"
salary ="no"
if Good == "yes" and salary =="yes" :
    print ("your are a genius")
elif Good !="yes" and salary == "yes":
    print ("you are only a good person")
elif Good =="yes" and salary!= "yes":
    print ("you should work hard")
else :
    print ("must try hard")

#Nested if
age = 67
own_car ="no"
if (age >=18):
    if (own_car == "yes"):
        print("you can drive")
    else :
        print("work hard and purchase a car")
else :
    print("grow up kid")


