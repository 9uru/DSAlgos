def merge1(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    index1 = index2 = 0

    new_arr = []
    while index1 < len(arr1) or index2 < len(arr2):
        if index1 == len(arr1):
            new_arr.append(arr2[index2])
            index2 += 1
        elif index2 == len(arr2):
            new_arr.append(arr1[index1])
            index1 += 1

        elif arr1[index1] <= arr2[index2]:
            new_arr.append(arr1[index1])
            index1 += 1
        elif arr1[index1] > arr2[index2]:
            new_arr.append(arr2[index2])
            index2 += 1

    return new_arr


print(merge1([0, 1, 4, 5], [2, 3, 4, 6, 7]))