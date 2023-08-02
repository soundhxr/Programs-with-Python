print("This program will let you calculate the sum of multiples of n in a series of consecutive natural numbers")
b = int(input("Enter the first number of the series: "))
c = int(input("Enter the last number of the series: "))
n = int(input("Enter the value of n: "))
a = list(range(b, c+1))
total = 0
for i in a:
    if i % n == 0:
        total += i
print("The sum of multiples of",n,"between",b,"and",c,"is",total)
        
