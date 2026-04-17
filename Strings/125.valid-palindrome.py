#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#Traverse the string
 #Store only alphanumeric characters in a list
 #Convert all characters to lowercase
 #Compare the list with its reverse
 #If both are same → palindrome, else not 
 # Space complexity : O(n) Time Complexity : O(n)

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = []

        for ch in s:
            if ch.isalnum():
                new_str.append(ch.lower())
        
        if new_str == new_str[ ::-1]:
            return True
        else:
            return False
    

        
# @lc code=end

