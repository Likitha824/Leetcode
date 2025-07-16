class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        original=str(x)
        reverse=str(abs(x))[::-1]
        if original==reverse:
            return True
        else:
            return False
        