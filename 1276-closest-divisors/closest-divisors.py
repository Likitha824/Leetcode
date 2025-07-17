class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def finddivisors(x):
            temp=[]
            find_till=int(math.sqrt(x))
            for j in range(find_till+1,0,-1):
                if x%j==0:
                    temp.append(j)
                    temp.append(x//j)
                    return temp
        list1=finddivisors(num+1)
        list2=finddivisors(num+2)
        if abs(list1[0]-list1[1])<abs(list2[0]-list2[1]):
            return list1
        else:
            return list2
        
                    
