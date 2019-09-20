def selection_sort(array):
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
    return array

def bubble_sort(array):
    for i in range(0,len(array)-1):
        for j in range(0, len(array)-1-i):
            if array[j] > array [j+1]:
                a = array[j+1]
                b = array[j]
                array[j] = a
                array[j+1] = b
    return array

def insertion_sort(array):
    for i in range(1,len(array)):
        A = array[i]
        for j in range(i-1,-1,-1):
            if A < array[j]:
                B = array[j]
                array[j] = A
                array[j+1] =B
    return array


array = [64, 25, 12, 22, 11]

ordered = selection_sort(array)
print("[selection sort result]")
print(ordered)

ordered = bubble_sort(array)
print("[bubble sort result]")
print(ordered)

ordered = insertion_sort(array)
print("[bubble sort result]")
print(ordered)
