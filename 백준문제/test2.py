x = -123

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        min_str = strs[0]
        for i in strs:
            if len(i) < len(min_str):
                min_str = i
        
        Str = min_str
        left = 0
        right = len(min_str)
        k = 0
        for i in strs:
            while Str:
                if Str in i:
                    break
                else:
                    if Str[-1] == min_str[-1]:
                        left = 0
                        right = len(min_str)
                        k += 1
                        Str = min_str[left:right-k]
                    else:
                        left += 1
                        right += 1
                        Str = min_str[left:right-k]
        return Str