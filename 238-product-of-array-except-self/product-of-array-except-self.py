class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prefix=1
        for i in range(1,len(nums)):
            prefix=prefix*nums[i-1]
            res[i]=prefix
        #print(res)
        postfix=1
        for i in range(n-2,-2,-1):
            res[i+1]=postfix*res[i+1]
            #print(res)
            postfix*=nums[i+1]
            #print(postfix)
        return res



          
'''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        for i in range(1, n):
            left_product[i] = nums[i - 1] * left_product[i - 1]
            print(left_product)
        right_product = [1] * n
        for i in range(n - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]
            print(right_product)
        output = []
        for i in range(n):
            output.append(left_product[i] * right_product[i])
        return output'''

# for smallers inputs o(n^2)
'''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(0,len(nums)):
            product=1
            for j in range(len(nums)-1,-1,-1):
                if i==j:
                    continue
                else:
                    print(i,j)
                    print(nums[j])
                    sign=1 if nums[j]>=0 else -1
                    product=sign*product*abs(nums[j])
                    print(product)
            list1.append(product)
        return list1'''

                

            

                

            