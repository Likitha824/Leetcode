class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=-1 if x<0 else 1
        x=abs(x)
        reverse=0
        while x:
            digit=x%10
            reverse=reverse*10+digit
            x=x//10
        reverse=sign*reverse
        if reverse< -2**31 or reverse >2**31:
            return 0
        else:
            return reverse
