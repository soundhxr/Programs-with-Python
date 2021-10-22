def gcd(numlist):
    mini = min(numlist) 
    factors = []
    for i in range(1, mini + 1):
        if mini % i == 0:
            factors.append(i)
    lst1 = numlist + factors  # Concept applied: The GCD must be one of the factors of "the smallest number of the list"
    lst1.sort()
    gcd = 1
    for i in lst1:
        count = 0
        for j in numlist:
            if j % i == 0:
                count += 1
            elif j % i != 0:
                break
            if count == len(numlist):
                gcd = i
    return gcd

print(gcd([4, 8, 924]))


        
        
