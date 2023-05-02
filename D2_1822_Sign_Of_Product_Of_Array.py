class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        cn=0
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                cn+=1
        if cn%2==0:
            return 1
        return -1
