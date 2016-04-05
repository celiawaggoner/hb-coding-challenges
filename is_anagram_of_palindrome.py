def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    #create an empty dictionary
    seen = {}

    #update count for each letter in the word
    for letter in word:
        if letter not in seen:
            seen[letter] = 1
        else:
            seen[letter] += 1

    #the word is a palindrome if there are 0 or 1 letters with an odd count

    odd_count = False

    for value in seen.values():
        if value % 2 != 0:
            if odd_count:
                return False
            odd_count = True
            
    return True


print is_anagram_of_palindrome("arceace")
#True

print is_anagram_of_palindrome("arceaceb")
#False
