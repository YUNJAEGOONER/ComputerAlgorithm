array = [64,25,12,22,11]

for i in range(1,len(array)):
    A = array[i]
    for j in range(i-1,-1,-1):
        if A < array[j]:
            B = array[j]
            array[j] = A
            array[j+1] =B
print(array)
