class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        #check first string character by character by other srtings
        for i in range(0,len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return result
            result=result+strs[0][i]
        return result
             
