lst = [1, 2, 3, 4, 5, 1, 2, 3]

def sub(lst):
    subarray_len = []
    count = 0
    for i in range(len(lst)):
        subarray_len.append(count)
        lst1 = lst[i:]
        count = 0
        for j in range(len(lst1)):
            if lst1[j] not in lst1[:j]:
                count += 1
            else:
                break
    return max(subarray_len)

print(sub(lst))
