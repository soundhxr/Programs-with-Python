print("Task: To find the no. of possible ways in which number N can be represented as the sum of two positive integers")
N = int(input("Enter the value of N: "))
no_of_ways = 0
for i in range(1, (N//2)+1):
    for j in range((N//2), N):
        if i + j == N:
            no_of_ways += 1
            print(i,"+",j,"=",N)
print("Answer: ",no_of_ways,"possible ways")
