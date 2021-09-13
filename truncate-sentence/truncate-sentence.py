class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        list1 = s.split()
        print(list1)
        if len(list1) > k:
            #use slice technique to truncate aka shorten
            return " ".join(list1[:k])
        return s