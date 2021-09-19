class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #string into list
        s_list=list(s)
        t_list=list(t)
        #sort the list
        s_list.sort()
        t_list.sort()
        #compare the list
        if s_list==t_list:
            return True
        else:
            return False