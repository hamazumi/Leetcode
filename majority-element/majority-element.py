class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
                print(d)
        return max(d,key=d.get)