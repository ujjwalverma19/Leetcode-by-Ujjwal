class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output=0
        for i in sentences:
            words=i.count(" ")+1
            if words > output:
                output=words
        return output
