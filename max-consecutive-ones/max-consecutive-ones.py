class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # keep track of counter
        # keep track of high score
        
        # go over the list
            # if encounter a 1, increment counter
            
            #compare counter to high score.
            # if current counter greater, update high score
            
            # else encounter a 0
                #reset the counter
                
        # return high score
        
        counter = 0
        high_score = 0
        
        for i in nums:
            if i == 1:
                # = to counter = counter + 1
                counter += 1
                high_score = max(counter, high_score)
                
            else:
                #reset the counter
                counter = 0
            
        return high_score