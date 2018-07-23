import pyprimes
from challenges.entry.src.fizzbuzz import FizzBuzz


def test_fizzbuzz():

    prime = pyprimes.primes_above(5)
    assert FizzBuzz.fizzbuzz(i=next(prime) * 3) == 'fizz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 3) == 'fizz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 3) == 'fizz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 5) == 'buzz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 5) == 'buzz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 5) == 'buzz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 15) == 'fizzbuzz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 15) == 'fizzbuzz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 15) == 'fizzbuzz'
