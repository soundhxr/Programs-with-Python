print("Enter as many numbers as you want and Find their sum, the highest and the lowest number")
n1 = int(input("Enter no: "))
list1 = [n1]
while input("press q to quit or press Enter key to continue - ") != 'q':
    n = int(input("Enter no: "))
    list1.append(n)
    n1 += n
print("The sum of the numbers you entered is",n1)
print("The highest number is",max(list1),"and The lowest number is",min(list1))
print("Numbers entered: ", *list1)

