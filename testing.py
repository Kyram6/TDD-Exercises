from math import floor

#1. check even number
def is_even(number):
    return number % 2 == 0

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False


#2. get intials
def test_get_intials():
    assert get_initials("Kyram T Ngoma") == "KTN"

def get_initials(name):
    return "".join(word[0].upper() for word in name.split()) 

