class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        while(right<len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                #print(nums)
                #print(left)
                left=left+1
            right=right+1
            