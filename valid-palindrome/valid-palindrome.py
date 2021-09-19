class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(s)
        res=""
        for x in s:
            if x.isalnum():
                res+=x
        res=res.lower()
        return res==res[::-1]