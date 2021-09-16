class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        length = len(set(sentence))
        if length == 26:
            return True
        
#set() returns takes away any duplicates