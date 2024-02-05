def swapList(list):
    size = len(list)

    temp = list[0]
    list[0] = list[size - 1]
    list[size - 1] = temp

    return list

list = [1, 2, 3, 4, 5]

print(swapList(list))