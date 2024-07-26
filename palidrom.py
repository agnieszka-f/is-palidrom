def is_palidrom(word):
    """
    The function checks if a given word is a palindrome
    Arguments:
    word
    Return value:
    True or False
    """
    reversed_word = word[::-1]
    return word == reversed_word

print(is_palidrom('kajak'))
print(is_palidrom('kwiat'))