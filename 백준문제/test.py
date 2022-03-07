class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPal = 0
        maxPal = ""
        start = 0
        while start+longestPal < len(s):
            s_list = list(s[start:start+longestPal])
            for i in range(start+longestPal,len(s)):
                s_list.append(s[i])
                s_list_reverse = s_list.copy()
                s_list_reverse.reverse()
                if s_list == s_list_reverse:
                    longestPal = i-start+1
                    maxPal = s[start:i+1]
                    print(i, longestPal, maxPal)
            start += 1
        return maxPal
            
s = Solution()
print(s.longestPalindrome("babad"))