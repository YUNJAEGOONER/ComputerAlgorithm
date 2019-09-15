array = [11,25,12,22,64]


for i in range(0,len(array)):
    A = array[i]
    for j in range(i+1, len(array)):
        if A > array[j]:
            A = array[j]
    n = 0
    for k in range(0,len(array)):
        if A != array[k]:
            n = n + 1
        else:
            B = array[i]
            array[i] = array[n]
            array[n] = B
    print(array)
