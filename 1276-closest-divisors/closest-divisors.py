class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def finddivisors(x):
            divisors=[]
            int(math.sqrt(x))
            for j in range(int(math.sqrt(x)),0,-1):
                if x%j==0:
                    divisors.append(j)
                    divisors.append(x//j)
                    return divisors
        res1=finddivisors(num+1)
        res2=finddivisors(num+2)
        if abs(res1[0]-res1[1])<abs(res2[0]-res2[1]):
            return res1
        else:
            return res2
        
                    
