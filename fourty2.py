#Map

marks=[39,46,76,86,24,79,99]
def grade(marks):
    if marks >=90:
        return "A"
    elif marks >=80:
        return "B"
    elif marks >=70:
        return "C"
    elif marks >=60:
        return "D"
    else:
        return "F"
grades=list(map(grade,marks))
print(grades)

#Filter
marks=[39,46,76,86,24,79,99]
def failure(marks):
    if marks <=60:
        return "F"
result=filter(failure,marks)
print("Failing score is ",list(result))