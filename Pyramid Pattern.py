print("Task: To print palindromic pyramid pattern using numbers")
r = int(input("Enter no. of rows of the pyramid you want to print: "))
print("\n")

# method1
"""lst = list(range(1, r+1))
for i in lst:
    print("  "*(len(lst)-i),*lst[:i-1],i,*lst[:i-1][::-1])"""

# method2
for j in range(1, r+1):
    print("  " * (r-j), end="")
    num = 0
    while num != j:
        num += 1
        print(num, end=" ")
    while num != 1:
        num -= 1
        print(num, end=" ")
    print(end="\n")