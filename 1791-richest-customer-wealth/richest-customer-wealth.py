class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output=0
        for i in accounts:
            total=0
            for j in i:
                total+=j
            if total > output:
                output=total
        return output