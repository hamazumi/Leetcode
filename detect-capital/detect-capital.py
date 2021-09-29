class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word == word.capitalize():     # capitalize() turns the first letter capital and the rest are turned lowercase
            return True
        else:
            return False