# Given a list of numbers,
# find the maximum sum of K CONSECUTIVE integers from the list

def bruteForce_maxSum(arr, k):
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i+j]
        max_sum = max(max_sum, current_sum)
    return max_sum

arr = [80, -50, 90, 100]
print(bruteForce_maxSum(arr, 2))

def SlidingWIndow(arr, windowSize):
    n = len(arr)
    if windowSize>=n:
        print("Window big enough to fill the list")
        return -1
    
    window_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = window_sum
    for i in range(n-windowSize):
        window_sum = window_sum + arr[i+windowSize] - arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum

arr = [2,4,6,3,1,8]
print(SlidingWIndow(arr, 2))