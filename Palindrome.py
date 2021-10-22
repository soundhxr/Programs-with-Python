num=int(input("Enter number: "))
rev=0
num2=num
while num>0:
    rem=num %10
    rev=rev*10+rem
    num//=10
if rev == num2:
    print(num2,"is a palindrome")
else:
    print(num2,"is not a palindrome")
