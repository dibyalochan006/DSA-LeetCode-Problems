#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        map_t_s = {}

        for c1, c2 in zip(s, t):
            if c1 in map_s_t:
                if map_s_t[c1] != c2:
                    return False 
            else:
                map_s_t[c1] = c2
            if c2 in map_t_s:
                if map_t_s[c2] != c1:
                    return False 
            else:
                map_t_s[c2] = c1
        return True
        
# @lc code=end

