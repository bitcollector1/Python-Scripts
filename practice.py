###################################################################################################################
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
###################################################################################################################
def tup(*args):
    print(list(args))
    print(args)

tup(input("\nPlease enter a sequence of numbers\n"))

###################################################################################################################
# Test for palindrome - Rats live on no evil star
###################################################################################################################
def palindrome(message):
    while message:
        if message[0] == message[-1]:
            message.pop(0)
            message.pop()
        else:
            break

    if not message:
        print("Your string IS a palindrome")
    else:
        print("Your string IS NOT a palindrome")


if __name__ == '__main__':

    palindrome(list(input("\nInput string to test palindrome\n").replace(" ", "").lower()))

###################################################################################################################
# Write a function that converts the input to the output
# Output: [("a", 4), ("b", 3), ("c", 2), ("a", 1)]
###################################################################################################################

input_string = "aaaabbbcca"

from itertools import groupby
[(k, len(list(g))) for k, g in groupby(input_string)]

############################################################################################################################################
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
############################################################################################################################################

s = "Revese all of the words in this string."

class Solution(object):    
    def reverseWords(self, s: 'str') -> 'str':
        return " ".join(i[::-1] for i in s.split())

my_solution = Solution()
my_solution.reverseWords(s)    


############################################################################################################################################
# Find out if the same value makes up at least 50% of the total elements in a list
############################################################################################################################################

from collections import Counter

test = [1,2,3,4,5,2,2,2,2,5]

def fifty(*args):
    c = Counter(test).most_common(1)
    for key,value in c:
        k = key
        v = value
    percent = v / len(test)
    if percent >= .50:
        print(f"The list is {round(percent, 2)}% full. {k} was found {v} times out of {len(test)} total elements")
    else:
        print(f"The list is {round(percent, 2)}% full. {k} was found {v} times out of {len(test)} total elements")


if __name__ == "__main__":
    fifty()

############################################################################################################################################
# Find all substrings in string, including overlap
############################################################################################################################################

# Find all substrings in string, including overlap
ini_str = "GeeksforGeeksforGeeksforGeeks"
sub_str = 'GeeksforGeeks'
 
# Count of substrings using startswith 
res = sum(1 for i in range(len(ini_str)) if ini_str.startswith(sub_str, i)) 

print(f"Number of substrings {sub_str} found: {res} ")

