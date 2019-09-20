array = [1,2,4,3,5]

for i in range(0,len(array)-2):
    flag = True
    for j in range(0, len(array)-1-i):
        if array[j] > array [j+1]:
            a = array[j+1]
            b = array[j]
            array[j] = a
            array[j+1] = b
            flag = False
    if flag == True:
        break

print(array)
