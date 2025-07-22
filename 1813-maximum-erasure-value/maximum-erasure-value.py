class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=0
        right=0
        sum1=0
        list1=[]
        max_sum=0
        while(right<len(nums)):
            if nums[right] in list1:
                while nums[right] in list1:
                    list1.remove(nums[left])
                    #print(list1)
                    sum1=sum1-nums[left]
                    left=left+1
            list1.append(nums[right])
            #print(list1)
            sum1=sum1+nums[right]
            max_sum=max(max_sum,sum1)
            right=right+1
        return max_sum

        