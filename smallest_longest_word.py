print("Task: to find the longest word(s) and the shortest word(s) in english which does not contain the letters you enter")
file = open("words.txt", "r")
lst = []
bad_letters = input("Enter the letters the word(s) should not include: ")
for i in file:
    for k in list(bad_letters):
        if k in i[:-1]:
            break
    else:
        lst.append(i[:-1])
maxi, mini = max([len(c) for c in lst]), min([len(c) for c in lst])
if mini == 1:
    mini = 2
print("\nLongest word(s):\n")
for word in lst:
    if len(word) == maxi:
        print(word)
print("\nSmallest word(s):\n")
for word in lst:
    if len(word) == mini:
        print(word)
