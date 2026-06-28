class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n={}
        for i in nums:
            n[i]=n.get(i,0)+1
            if n[i ]> len(nums)//2:
                return i