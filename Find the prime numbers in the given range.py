while True:
    mini = int(input("Enter minimum limit: "))
    maxi = int(input("Enter maximum limit: "))
    if maxi > 1 and mini > 1:
        break
    else:
        print("\nMinimum limit and Maximum limit should be greater than 1\n")

num_list = list(range(mini, maxi+1))
prime = []
for num in num_list:
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        prime.append(num)
if len(prime) == 0:
    print("There are no prime numbers in the given range.")
else:
    print("There are", len(prime), "prime numbers in the given range. They are", end=" ")
    print(*prime, sep=", ")
