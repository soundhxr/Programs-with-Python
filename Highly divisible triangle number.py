print("Task: Find the value of the first triangle number to have over 'N' divisors")
div = int(input("Value for N: "))
n = 0
i = 0
while True:
    i += 1
    n += i
    divisors = [j for j in range(1, n+1) if n%j == 0]
    if len(divisors) > div:
        print(n,"is the first triangle number to have over",div,"divisors")
        break
    else:
        divisors.clear()