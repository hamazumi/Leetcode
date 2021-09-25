class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s2=s*2
        print(s2)
        if goal in s2 and len(s)==len(goal):
            return True
        return False