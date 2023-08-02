num = int(input("Enter Number: "))
while num<=1:
    num = int(input("Enter Number higher than 1: "))
factors = [1,num]
for i in range(2,num):
    if num%i == 0:
        factors.append(i)
if len(factors) > 2:
    print(num,"is a composite number")
else:
    print(num,"is a prime number")
factors.sort()
print("Factors of",num,"are:",factors)
print("No. of Factors: ",len(factors))

