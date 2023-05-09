class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        n=len(mat)
        for i in range(len(mat)):
            summ+=mat[i][i]
        j=0
        while j<n:
            summ+=mat[n-j-1][j]
            j+=1
        if n%2==0:
            return summ
        mid=n//2
        return summ-mat[mid][mid]


