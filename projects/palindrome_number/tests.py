import unittest
from main import palindrome


class TestPalindrome(unittest.TestCase):
    def test_palindrome_returns_correct_message(self):
        result = palindrome(212)
        self.assertEqual(result, "212 is a palindrome")

    def test_non_palindrome_number_returns_correct_message(self):
        result = palindrome(123)
        self.assertEqual(result, "123 is not a palindrome")

    def test_palindrome_function_raises_TypeError_exception(self):
        with self.assertRaises(TypeError):
            palindrome("asd")


if __name__ == "__main__":
    unittest.main()
