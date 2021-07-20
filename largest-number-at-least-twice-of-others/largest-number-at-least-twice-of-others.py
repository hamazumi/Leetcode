class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
   
        largest = -1
        second_largest = -1
        result_index = -1
        
        for index, i in enumerate(nums):
            if i > largest:
                second_largest = largest
                largest = i
                result_index = index
                
                
            elif i > second_largest:
                second_largest = i
             
        if largest < second_largest*2:
            return -1
                
        return result_index
        
        