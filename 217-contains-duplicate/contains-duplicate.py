class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums))<len(nums):
            return True
        else:
            return False

            
            
#three methods
#1.using two for loops(o(n2)) and o(1)
#2.using sort method sort and check two consequeitive elements time (o(nlogn)) space o(1)
#3.set time and space (o(n))
