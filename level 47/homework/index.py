#homework1
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
#homework2
def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count
#homework3
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

#homework4
def reverse_string(text):
    return text[::-1]

#homework5
def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
