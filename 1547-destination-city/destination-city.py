class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        output=[]
        for i in paths:
            output.append(i[0])
        for j in paths:
            if j[1] not in output:
                return j[1]