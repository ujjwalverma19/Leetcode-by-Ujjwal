class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans, stk = [0] * n, []
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] < h:
                ans[stk.pop()] += 1
            if stk:
                ans[stk[-1]] += 1
            stk.append(i)
        return ans
