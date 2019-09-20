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


array = [64, 25, 12, 22, 11, 2]
ordered = mergeSort(array)
print(ordered)
