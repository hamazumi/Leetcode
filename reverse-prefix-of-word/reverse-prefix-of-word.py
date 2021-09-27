class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x = word.find(ch)
        
        if x==-1:
            return word
            
        else:
            word = word[:x+1][::-1] + word[x+1:]
            return word