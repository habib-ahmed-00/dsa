def binary_search(array, target):
    '''
    Binary search: Divide and Conquer O(N*logN)
    '''
    left = 0
    right = len(array) - 1
    while (left <= right):
        mid = (left+right)//2
        if array[mid] == target:
            return mid
        elif (array[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    goal = 7
    result = binary_search(arr, goal)
    if result != -1:
        print("Element found: ", result)
    else:
        print("Element not found")
