Problem Statement:

Given a string as an input. We need to write a program that will print all non-empty substrings of that given string.

Examples : 

Input :  abcd
Output :  a 
          b
          c
          d
          ab
          bc
          cd
          abc
          bcd
          abcd
We can run three nested loops, the outermost loop picks starting character, mid loop considers all characters on right of the picked character as ending character of substring. The innermost loop prints characters from currently picked starting point to picked ending point. 

Solution:

# Python3 program to print all possible
# substrings of a given string


# Function to print all sub strings
def subString(Str,n):
	
	# Pick starting point
	for Len in range(1,n + 1):
		
		# Pick ending point
		for i in range(n - Len + 1):
			
			# Print characters from current
			# starting point to current ending
			# point. 
			j = i + Len - 1

			for k in range(i,j + 1):
				print(Str[k],end="")
			print()
			
# Driver program to test above function
Str = "abc"
subString(Str,len(Str))

# This code is contributed by mohit kumar


Output: 

a
b
c
ab
bc
abc
Method 2 (Using substr() function) 
s.substr(i, len) prints substring of length ‘len’ starting from index i in string s.


Method 2 (Using substr() function) 
s.substr(i, len) prints substring of length ‘len’ starting from index i in string s.

	
# Python program to print all possible
# substrings of a given string

# Function to print all sub strings
def subString(s, n):
	# Pick starting point in outer loop
	# and lengths of different strings for
	# a given starting point
	for i in range(n):
		for len in range(i+1,n+1):
			print(s[i: len]);

# Driver program to test above function
s = "abcd";
subString(s,len(s));

# This code is contributed by princiraj1992


Output: 

a
ab
abc
abcd
b
bc
bcd
c
cd
d


Method 3 (Generate a substring using previous substring)

'''
* Python3 program to prall possible
* substrings of a given string
* without checking for duplication.
'''


'''
* Function to prall (n * (n + 1)) / 2
* substrings of a given string s of length n.
'''
def printAllSubstrings(s, n):

	# Fix start index in outer loop.
	# Reveal new character in inner loop till end of string.
	# Prtill-now-formed string.
	for i in range(n):
		temp=""
		for j in range(i,n):
			temp+=s[j]
			print(temp)

# Driver program to test above function

s = "Geeky"
printAllSubstrings(s, len(s))

# This code is contributed by shubhamsingh10


Output: 

G
Ge
Gee
Geek
Geeky
e
ee
eek
eeky
e
ek
eky
k
ky
y


Another:

By considering the length 
def solve(s):
    n = len(s)
    for i in range(1, n+1):
        for j in range(0, n):
            if j+i<=n:
                print(j, j+i, s[j:j+i])
            
solve("abcde")

Output:

0 1 a
1 2 b
2 3 c
3 4 d
4 5 e
0 2 ab
1 3 bc
2 4 cd
3 5 de
0 3 abc
1 4 bcd
2 5 cde
0 4 abcd
1 5 bcde
0 5 abcde



