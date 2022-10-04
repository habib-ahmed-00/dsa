'''
3. Longest Substring Without Repeating Characters
Medium
29.1K
1.2K
Companies
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

def longestSubstring_bruteForce(s):
    maxLength = 0
    n = len(s)
    if n<=1:
        return n
    for i in range(n):
        hashmap = {}
        currentLength = 0
        for j in range(i,n):
            if s[j] not in hashmap:
                hashmap[s[j]] = True
                currentLength+=1
            else:
                maxLength = max(currentLength,maxLength)
                currentLength = 0
                break
    return maxLength

# print(longestSubstring_bruteForce('bbbbb'))


def longestSubstring_OPTIMIZED(s):
    maxLength = 0
    n = len(s)
    if n<=1:
        return n
    left = right = 0
    hashmap = {}
    while right<n and left<n:
        currentCharacter = s[right]
        if currentCharacter in hashmap:
            prevCharacter = hashmap[currentCharacter]
            left = max(left, prevCharacter+1)
        hashmap[currentCharacter] = right
        maxLength = max(maxLength, right-left+1)
        right+=1

    return maxLength

print(longestSubstring_OPTIMIZED('bbbbb'))