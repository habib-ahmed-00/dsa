"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

def BruteForce_WaterContainer(arr):
    n = len(arr)
    maxArea = 0
    if n<=1:
        return 0

    for i in range(n):
        for j in range(i+1,n):
            length = min(arr[j],arr[i])
            width = j-i
            area = length*width
            maxArea = max(maxArea,area)
    
    return maxArea

print(BruteForce_WaterContainer([1,8,6,2,5,4,8,3,7]))


def optimized_WaterContainer(arr):
    n = len(arr)
    maxArea = 0
    left = 0
    right = n-1
    while left<right:
        length = min(arr[left],arr[right])
        width = right-left
        area = length*width
        maxArea = max(maxArea,area)
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    return maxArea

print(optimized_WaterContainer([1,8,6,2,5,4,8,3,7]))