class Solution:
    def average(self, salary: List[int]) -> float:
        n=len(salary)
        minn=maxx=salary[0]
    
        
        summ=0
        for i in range(n):
            if salary[i]>maxx:
                maxx=salary[i]
            elif salary[i]<minn:
                minn=salary[i]
           
            summ+=salary[i]
       
        return (summ-minn-maxx)/(n-2)
