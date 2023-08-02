from itertools import permutations
print("Task: To find all the N digit numbers (whose digits are distinct) that can be formed using the digits you enter")
N = int(input("\nEnter a value for N: "))
s = ""
for k in range(int(input("\nHow many digits are you going to enter? - "))):
    s += str(int(input("Enter a distinct digit: ")))
lst = []
print()
for i in permutations(s, N):
    num = (int("".join(i)))
    if len(str(num)) == N:
        print(num)
        lst.append(1)
print("\n"+str(len(lst)),"number(s) can be formed by using the given digits.")
