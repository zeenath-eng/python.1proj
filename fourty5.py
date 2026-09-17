class stack:
    def __init__(self):
        self.items = []
    def push(self,x):
        self.items=[x]+self.items
    def pop(self):
        return self.items.pop(0)
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.items)
print(s.pop())
print(s.items)
s.push(8)
print(s.items)
print(s.pop())
print(s.items)