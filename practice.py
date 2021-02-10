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


def countchars(input_string):
    result = []
    count = 1

    for i, letter in enumerate(input_string):
        if len(input_string) > i + 1 and letter == input_string[i + 1]:
            count += 1
        else:
            result.append((letter, count))
            count = 1

    return result


countchars(input_string)
