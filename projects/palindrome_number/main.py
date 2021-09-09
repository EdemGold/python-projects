def palindrome(num):
    num = str(num)
    return f'{num} is a palindrome' if (num[::-1]) == num else f'{num} is not a palindrome'


usr_inp = input('Enter a number or string to check if palindrome: ')
print(palindrome(usr_inp))