array = [64, 25, 12, 22, 11]

for i in range(0,len(array)-1):
    for j in range(0, len(array)-1-i):
        if array[j] > array [j+1]:
            a = array[j+1]
            b = array[j]
            array[j] = a
            array[j+1] = b
print(array)
