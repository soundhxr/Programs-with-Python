a = int(input("Enter the first number: "))
b = int(input("Enter the last number: "))
import math
print("The following numbers are the perfect squares between",a,"and",b)
for i in range(a+1, b):
    if math.sqrt(i) in range(int(math.sqrt(a)), int(math.sqrt(b))+1):
        print("The square of",int(math.sqrt(i)),"is",i)

