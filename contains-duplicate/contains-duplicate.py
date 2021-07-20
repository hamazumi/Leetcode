class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         # using a dictionary as a hash table
        hash_table = {}
        # loop over the numbers
        for num in nums:
            # if the number is in the hash table -- return immediately
            if num in hash_table:
                return True
            # otherwise add the number to the hash table so it can be found
            else:
                hash_table[num] = num

        # otherwise return False if no match is found
        return False
        
   