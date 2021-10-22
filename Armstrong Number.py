n = int(input("Enter any number: "))
num = n
no_of_digits = len(str(n))
s=0
while n>0:
    d = n%10
    s += d**no_of_digits
    n//=10
if s == num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
    
    
