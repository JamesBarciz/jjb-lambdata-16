# Example function (Enlarge)

def enlarge(n):
    '''
    Param n is a number

    Function will enlarge the number (x 100)
    '''
    return n * 100

# # Ask for user input

# y = int(input('Please choose a number!'))
# print(y, enlarge(y))

# Only when this script is ran, run these statements
# Otherwise, only use above function

if __name__ == "__main__":
    print("Hello!")
    y = int(input('Please choose a number!'))
    print(y, enlarge(y))
