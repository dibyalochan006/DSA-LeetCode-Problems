#
# @lc app=leetcode id=1903 lang=python3
#
# [1903] Largest Odd Number in String
## 1903. Largest Odd Number in String
/* # 1903. Largest Odd Number in String

## 💡 Approach

* Traverse from right to left
* Find first odd digit
* Return substring from start to that index
* If no odd digit → return ""

---

## ⏱️ Time Complexity

O(n)

---

## 📦 Space Complexity

O(1)
*/

# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n =len(num)  
        for i in range(n-1 ,-1,  -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""
        
# @lc code=end

