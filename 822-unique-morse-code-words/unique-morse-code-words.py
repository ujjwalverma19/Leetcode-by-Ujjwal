class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-","-...","-.-.","-..",".",
            "..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",
            ".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        transformations = []
        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            if code not in transformations:
                transformations.append(code)
        return len(transformations)