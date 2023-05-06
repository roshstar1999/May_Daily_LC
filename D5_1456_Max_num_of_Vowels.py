class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start=0
        end=k
        maxx=0
        countt=0
        n=len(s)
        for i in range(k):
            if s[i] in 'aeiou':
                countt+=1
        maxx=countt
        
        

        while end<n:
            if s[start] in 'aeiou':
                countt-=1
            if s[end] in 'aeiou':
                countt+=1
            start+=1
            end+=1
            maxx=max(countt,maxx)



        return maxx
