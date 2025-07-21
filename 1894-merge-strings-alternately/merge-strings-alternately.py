class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       n1=0
       n2=0
       res=""
       while n1<len(word1) or n2<len(word2):
        if n1<len(word1):
            res+=word1[n1]
        if n2<len(word2):
            res+=word2[n2]
        n1=n1+1
        n2=n2+1
       return res



       