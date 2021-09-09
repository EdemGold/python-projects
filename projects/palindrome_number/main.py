def palindrome(num: int) -> str:
    """Given a number check if it is palindrome or not"""

    if not isinstance(num, int):
        raise TypeError("Please enter an integer")

    num = str(num)

    return (
        f"{num} is a palindrome" if (num[::-1]) == num else f"{num} is not a palindrome"
    )


if __name__ == "__main__":
    usr_inp = input("Enter a number or string to check if palindrome: ")
    print(palindrome(usr_inp))
