Problem Statement:

Given a binary string, that is it contains only 0s and 1s. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped.
Examples :

Input : str = “001”
Output : 1
Minimum number of flips required = 1
We can flip 1st bit from 0 to 1 

Input : str = “0001010111”
Output : 2
Minimum number of flips required = 2
We can flip 2nd bit from 0 to 1 and 9th 
bit from 1 to 0 to make alternate 
string “0101010101”.
Expected time complexity : O(n) where n is length of input string.

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
We can solve this problem by considering all possible results, As we are supposed to get alternate string, there are only 2 possibilities, alternate string starting with 0 and alternate string starting with 1. We will try both cases and choose the string which will require minimum number of flips as our final answer.
Trying a case requires O(n) time in which we will loop over all characters of given string, if current character is expected character according to alternation then we will do nothing otherwise we will increase flip count by 1. After trying strings starting with 0 and starting with 1, we will choose the string with minimum flip count.
Total time complexity of solution will be O(n)

Solution:

# Python 3 program to find minimum number of 
# flip to make binary string alternate 

# Utility method to flip a character 
def flip( ch): 
	return '1' if (ch == '0') else '0'

# Utility method to get minimum flips when 
# alternate string starts with expected char 
def getFlipWithStartingCharcter(str, expected): 

	flipCount = 0
	for i in range(len( str)): 
		
		# if current character is not expected, 
		# increase flip count 
		if (str[i] != expected): 
			flipCount += 1

		# flip expected character each time 
		expected = flip(expected) 
	return flipCount 

# method return minimum flip to make binary 
# string alternate 
def minFlipToMakeStringAlternate(str): 

	# return minimum of following two 
	# 1) flips when alternate strign starts with 0 
	# 2) flips when alternate strign starts with 1 
	return min(getFlipWithStartingCharcter(str, '0'), 
			getFlipWithStartingCharcter(str, '1')) 

# Driver code to test above method 
if __name__ == "__main__": 
	
	str = "0001010111"
	print(minFlipToMakeStringAlternate(str)) 

Reference: https://www.geeksforgeeks.org/number-flips-make-binary-string-alternate/ 