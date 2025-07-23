class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        if len(t)!=len(s):
            return False
        for char in s:
            hash1[char]=hash1.get(char,0)+1
            '''if char not in hash1:
                hash1[char]=1
            else:
                hash1[char]+=1
        #print(hash1)'''
        for char in t:
            '''if char not in hash2:
                hash2[char]=1
            else:
                hash2[char]+=1'''
            hash2[char]=hash2.get(char,0)+1
        #print(hash2)
        return hash1==hash2
