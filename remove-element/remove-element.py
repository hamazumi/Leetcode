class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, 0
        
        while k < len(nums):
            if nums[k] != val:
                nums[i] = nums[k]
                i += 1
            k += 1
        
        return i