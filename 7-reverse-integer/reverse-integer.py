class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lower_limit=-2**31
        upper_limit=2**31-1
        sign= -1 if x<0 else 1
        reverse_num=str(abs(x))[::-1]
        reverse_num=sign*int(reverse_num)

        if reverse_num <lower_limit or reverse_num>upper_limit:
            return 0
        else:
            return reverse_num