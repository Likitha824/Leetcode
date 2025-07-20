class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1={}
        for i in range(len(nums)):
            key=target-nums[i]
            if key in hash1:
                return hash1[key],i
            else:
                hash1[nums[i]]=i

'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]'''
