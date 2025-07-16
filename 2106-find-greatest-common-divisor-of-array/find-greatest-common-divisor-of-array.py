class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest=min(nums)
        largest=max(nums)
        remainder=0
        while largest%smallest!=0:
            smallest,largest=largest%smallest,smallest
        return smallest
            
            
