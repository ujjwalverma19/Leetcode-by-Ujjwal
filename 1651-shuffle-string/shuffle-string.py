class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
      output=[""]*len(s)
      for i in range(len(s)):
        output[indices[i]]=s[i]
        lesbian="".join(output)
      return lesbian

