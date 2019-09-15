array = [64,25,12,22,11]

for border in range(0,len(array)-1):
    min = border
    for pointer in range(border+1,len(array)):
        if array[min] > array[pointer]:
            min = pointer

    temp = array [border]
    array[border] = array[min]
    array[min] = temp

print(array)
