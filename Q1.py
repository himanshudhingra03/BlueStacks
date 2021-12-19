"""
/*
* Function to calculate number of possible
* permutations to make the given height of the tower
*
* Input: height -> int
* Returns: Permutations -> int
*/
"""


def findPermutations(height: int) -> int:
    if height < 0:
        return 0
    elif height == 1:
        return 1
    elif height == 2:
        return 2
    elif height == 3:
        return 4
    else:
        return (
            findPermutations(height - 1)
            + findPermutations(height - 2)
            + findPermutations(height - 3)
        )


# Main Driver Function
def main():
    try:
        height = int(input("Enter the Height: "))
        print(findPermutations(height))
    except ValueError:
        print("Please Enter an Integer Value.")
        main()


main()