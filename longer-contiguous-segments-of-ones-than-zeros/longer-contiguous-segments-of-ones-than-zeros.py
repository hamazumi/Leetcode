class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        counter_one = 0
        score_one = 0
        
        counter_zero = 0
        score_zero = 0
        
        for i in s:
            if i == '1':
                # = to counter = counter + 1
                counter_one += 1
                score_one = max(counter_one, score_one)
                counter_zero = 0
                   
            elif i == '0':
                counter_zero += 1
                score_zero = max(counter_zero, score_zero)
                counter_one = 0
                
        return score_one > score_zero
            
        