import time
import random

def Insertion_sort(array):
    for i in range(1,len(array)):
        A = array[i]
        for j in range(i-1,-1,-1):
            if A < array[j]:
                B = array[j]
                array[j] = A
                array[j+1] =B
    return array

n = 10000
unordered = []
for i in range(0,n):
    num = random.randint(1,n)
    unordered.append(num)

start = time.time()
Insertion_sort(unordered)
end = time.time()
print(end-start)

ordered = Insertion_sort(unordered)
print(ordered)
