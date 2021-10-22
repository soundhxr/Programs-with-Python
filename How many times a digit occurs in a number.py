n = int(input("Enter any number: "))
d = int(input("Enter any digit: "))
num = n
i = 0
while n > 0:
    s = n%10
    if s == d:
        i+=1
    n//=10
print("The digit",d,"occurs",i,"time(s) in",num)
    
