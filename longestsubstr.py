
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        all_lengths = []
        if len(s)==0:
            return 0
        # i = 0
        for j in range(len(s)):
            start = s[j]
            this_length = 1
            visited = [start]
            i = j + 1
            while i < len(s):
                # i = i + 1
                if s[i] in visited:
                    
                    break
                else:
                    visited.append(s[i])
                    this_length += 1
                i = i + 1
            all_lengths.append(this_length)
            if max(all_lengths) >= len(s)-j:
                break
        
        return max(all_lengths)
                
                