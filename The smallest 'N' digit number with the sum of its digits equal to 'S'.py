print("To find: The smallest 'N' digit number with the sum of its digits equal to 'S'")
s = int(input("Enter a value for S: "))
d = int(input("Enter a value for N: "))
for j in range(10**(d-1), 10**(d)):
    num = j
    sm = 0
    while j>0:
        l = j % 10
        sm += l
        j //= 10
    if sm == s:
        print(num)
        break
else:
    print("There is no",d,"digit number with sum of its digits equal to",s)
