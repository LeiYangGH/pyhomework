"""Print all the perfect squares from zero up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""

def read_bound(msg):
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly"""
   
    upper_bound = None
    while upper_bound is None:
        line = input(msg)
        if line.isnumeric():
            upper_bound = int(line)
            if upper_bound <= 0:
                print("You must enter a positive number.")
            else:
                return upper_bound
        else:
            print("You must enter a number.")
    #lower_bound = None
    #while lower_bound is None:
    #    line = input("Enter the lower bound: ")
    #    if line.isnumeric():
    #        lower_bound = int(line)
    #        return lower_bound
    #    else:
    #        print("You must enter a positive number.")

   
def is_perfect_square(num):
    """Return true if and only if num is a perfect square"""
    import math
    if int(math.sqrt(num)) == math.sqrt(num):
        return num



def print_squares(lower_bound, upper_bound, squares):
    """Print a given list of all the squares up to a given upper bound"""
    print("The perfect squares from {} to {} are: ".format(lower_bound, upper_bound))
    for square in squares:
        print(square, end=' ')
    print()
    # AND WHAT GOES HERE?

def main():
    """Every home should have one"""
    lower_bound = read_bound("Enter the lower bound: ")
    upper_bound = read_bound("Enter the upper bound: ")
    #lower_bound = 9
    #upper_bound = 99
    squares = []
    for num in range(lower_bound, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)

    print_squares(lower_bound, upper_bound, squares)

main()