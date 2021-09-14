class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = ['']*len(s)
        print(temp)
		# temporary list is created to hold all the characters.
        for i in range(len(s)):
			#Iterate through every letter in string 's' 
            temp[indices[i]] = s[i]
            print(temp)
			#Adds letters to new index position
            result = "".join(temp)
			#Converted to a string
        return result