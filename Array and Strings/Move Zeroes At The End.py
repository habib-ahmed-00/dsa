# Brute Force Approach
def MoveZeroes(arr):
    n = len(arr)
    output = list()
    for i in arr:
        if i != 0:
            output.append(i)
    m = len(output)
    for j in range(m,n):
        output.append(0)
    return output

arr = [0,1,4,24,0,77,86,00,77,23,11]
print(MoveZeroes(arr))


# Optimized Approach
def MoveZeroesOptimized(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    for k in range(j,n):
        arr[k] = 0
    return arr

arr = [0,1,4,24,0,77,86,00,77,23,11]
print(MoveZeroesOptimized(arr))
