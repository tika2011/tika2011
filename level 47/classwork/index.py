# 1
def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
# 2
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

# 3
def is_palindrome(word):
    word = word.lower() 
    return word == word[::-1]

# 4
def reverse_string(string):
    return string[::-1]

# 5
def longest_word(sentence):
    words = sentence.split()  
    return max(words, key=len)