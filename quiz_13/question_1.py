# Write a function that, given a letter, determines if it is a consonant.

def iscons(letter):
    vowels = 'aeiouAEIOU'
    
    if letter.isalpha() and letter not in vowels:
        return True
    else:
        return False