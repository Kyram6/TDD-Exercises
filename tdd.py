#1.
def is_even(number):
    return number % 2 == 0

#2.
def get_initials(name):
    return "".join(word[0].upper() for word in name.split())

# 3
def find_longest_word(word):
     return max(word,key=len)

#4
def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

# 5. count vowels

# 6. count words

# 7. most common item

# 8. palindrome

# 9. mask email address

# 10.discount

#11. grade scores

#12. calculate total cost of shopping basket

#13. passes and fails

#14. filter odd numbers

#15. shortest words
def find_shortest_word(words):
    return min(words, key=len)