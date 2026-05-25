class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        answer=[]
        for i in nums:
            total+=i
            answer.append(total)
        return answer