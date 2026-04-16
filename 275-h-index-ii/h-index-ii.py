class Solution:
    def hIndex(self,citations):
        n=len(citations)
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            paper=n-mid
            if citations[mid]>=paper:
                right=mid-1
            else:
                left=mid+1
        return n-left