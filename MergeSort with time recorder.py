import random
import time

def mergeSort(A):
    left =[]
    right =[]
    if len(A) <= 1:
        return A
    else:
        middle = int(len(A)/2)
        for i in range(0,middle):
            left.append(A[i])
        for i in range(middle,len(A)):
            right.append(A[i])
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left,right)

def merge(left,right):
    result = []
    while len(left) > 0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if len(left)>0:
        for i in range(0,len(left)):
            result.append(left[i])
    if len(right)>0:
        for i in range(0,len(right)):
            result.append(right[i])
    return result



n = 10000
unordered = []
for i in range(0,n):
    num = random.randint(1,n)
    unordered.append(num)

start = time.time()
mergeSort(unordered)
end = time.time()
print(end-start)

ordered = mergeSort(unordered)
print(ordered)
