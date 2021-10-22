class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
lst = []
marks=[]
high=[]
low=[]
no = int(input("How many students? "))
for i in range(no):
    s = student(input("enter student's name: "), int(input("student's marks: ")))
    lst.append(s)
    marks.append(s.marks)
maxi,mini = max(marks),min(marks)
for s in lst:
    if s.marks == maxi:
        high.append(s.name)
    elif s.marks == mini:
        low.append(s.name)
print('\nThe highest scorer(s) is/are',end=" ")
print(*high,sep=", ")

print('\nThe least scorer(s) is/are',end=" ")
print(*low,sep=", ")