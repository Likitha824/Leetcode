class Solution:
    def makeFancyString(self, s: str) -> str:
        res = [] 
        count = 1  
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count=count+1
                #print(count)
            else:
                count=1
            if count<3:
                res.append(s[i])
        return s[0]+"".join(res)


#method 2 using stack
'''class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=[]
        for char in s:
            if stack and stack[-1][0]==char:
                stack[-1][1]+=1
                if stack[-1][1]>=3:
                    stack[-1][1]=2
            else:
                stack.append([char,1])
            #print(stack)
        res="".join(char*count for char,count in stack)
        return res '''        

#first method
'''class Solution:
    def makeFancyString(self, s: str) -> str:
        output=""
        for char in s:
            if len(output)>=2 and char==output[-1] and char==output[-2]:
                continue
            else:
                output+=char
        return output'''