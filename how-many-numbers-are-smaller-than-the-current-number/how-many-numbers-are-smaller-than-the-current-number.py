class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #create list same length as nums
        new_list=[0]*len(nums)
        order=sorted(nums)
        j=0
        
        for i in nums:
            #.index() tells me the index number for i and replace new_list
            new_list[j]=order.index(i)

            j=j+1
        return new_list
        