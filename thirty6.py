class student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def average(self):
        return sum (self.score)/len(self.score)
    def display(self):
           print(self.name,self.age,self.score)

std1=student('zeenath',30,[90,67,97,98,87,69])
print(std1.name)
print(std1.average())
