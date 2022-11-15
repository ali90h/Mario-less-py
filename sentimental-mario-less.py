from cs50 import get_int

# main function


def main():
    height = get_height()
    for i in range(0, height, 1):
        for j in range(0, height, 1):
            if i + j < height - 1:
                print(" ", end="")
            else:
                print("#", end="")
        print()

# User input height function


def get_height():
    while True:
        # Get input height
        height = get_int("Height: ")
        if height > 0 and height < 9:
            break
    return height


main()
