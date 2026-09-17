def create():
    list = []
    i = 1
    while i <= 200:
        yield(i)
        i += 1


print(create())
x=create()
print(next(x))
print(next(x))
print(next(x))
print(list(x))