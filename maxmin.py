def maxmin(array):
    highest = array[0]
    lowest = array[0]
    for i in array:
        if i > highest:
            highest = i
        elif i < lowest:
            lowest = i
    return [lowest, highest]

print(maxmin([20,50,12,6,14,8]))