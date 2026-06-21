from math import floor
from tdd import *

#1. check even number
def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False

#2. get intials
def test_get_intials():
    assert get_initials("Kyram T Ngoma") == "KTN"

# 3. find longest word
def test_find_longest_word():
    assert find_longest_word(["dog", "lion", "supercalifragilistic"]) == "supercalifragilistic"

# 4. filter even number
def test_filter_even_numbers():
    assert filter_even_numbers([1,2,3,4,5,6,7]) == [2,4,6]

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
def test_find_shortest_word():
    assert find_shortest_word(["dog", "lion", "as"]) == "as"