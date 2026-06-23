class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        size = len(heights)
        res = [0] * size
        for i in range(size - 1, -1, -1):
            height = heights[i]
            visible = 0
            while stack and height > stack[-1]:
                stack.pop()
                visible += 1
            if stack:
                visible += 1
            stack.append(height)
            res[i] = visible
        return res
