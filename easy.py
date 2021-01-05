# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple

def tup(*args):
    print(list(args))
    print(args)

tup(input("\nPlease enter a sequence of numbers\n"))
