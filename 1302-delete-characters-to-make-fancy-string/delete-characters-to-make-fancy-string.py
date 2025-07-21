class Solution:
    def makeFancyString(self, s: str) -> str:
        output=""
        for char in s:
            if len(output)>=2 and char==output[-1] and char==output[-2]:
                continue
            else:
                output+=char
        return output