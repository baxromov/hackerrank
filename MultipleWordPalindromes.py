"""

There are numerous phrases that are palindromes when spacing is ignored. Examples
include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
among many others. Extend your solution to Exercise 75 so that it ignores spacing
while determining whether or not a string is a palindrome. For an additional challenge,
further extend your solution so that is also ignores punctuation marks and treats
uppercase and lowercase letters as equivalent.

"""


def is_multiple_word_palindromes(str):
    return True if str.strip().replace(" ", "") == str.strip().replace(" ", "")[::-1] else False


print(is_multiple_word_palindromes('some men interpret nine memos'))
