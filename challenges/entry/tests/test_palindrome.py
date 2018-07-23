from challenges.entry.src.palindrome import Palindrome


def test_is_palindrome():
    assert Palindrome.check_palindrome(s='racecar')
    assert Palindrome.check_palindrome(s='civic')
    assert Palindrome.check_palindrome(s='kayak')
    assert Palindrome.check_palindrome(s='madam')

    # Special Cases

    assert Palindrome.check_palindrome(s='b')
    assert Palindrome.check_palindrome(s='Racecar')
    assert Palindrome.check_palindrome(s='kayaK')
    assert Palindrome.check_palindrome(s='reDder')
    assert Palindrome.check_palindrome(s='Eva, Can I Stab Bats In A Cave?')


def test_is_not_palindrome():
    assert not Palindrome.check_palindrome(s='kitten')
    assert not Palindrome.check_palindrome(s='milkshake')
    assert not Palindrome.check_palindrome(s='stingray')
    assert not Palindrome.check_palindrome(s='psychic')
    assert not Palindrome.check_palindrome(s='We have a lot of rain in June.')
