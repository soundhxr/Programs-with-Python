no = int(input("How many terms of the Fibonacci series do you want to print? "))
n1 = 0
n2 = 1
I = 1
if no == 1:
    print(n1)
elif no == 2:
    print(n1,n2)
elif no <= 0:
    print("Enter a positive number!")
else:
    print(n1,n2,end= " ")
    for i in range(no-2):
        nth = n1 + n2
        print(nth,end=" ")
        n1,n2 = n2,nth