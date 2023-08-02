#Collatz_sequence

n = int(input("Enter Number: "))
i = 0
while n != 1:
    if n % 2 == 0:
        n = n//2
    else:
        n = 3*n + 1
    print(n)
    i += 1
print('it takes', i, 'operations to get one (1)')
    
