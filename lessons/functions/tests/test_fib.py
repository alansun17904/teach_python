from .context import Fibonacci as Fib


def test_fib():
    assert Fib.generate_fib(0) == 0
    assert Fib.generate_fib(1) == 1
    assert Fib.generate_fib(2) == 1
    assert Fib.generate_fib(3) == 2
    assert Fib.generate_fib(4) == 3
    assert Fib.generate_fib(5) == 5
    assert Fib.generate_fib(6) == 8
    assert Fib.generate_fib(7) == 13
    assert Fib.generate_fib(8) == 21
    assert Fib.generate_fib(9) == 34
    assert Fib.generate_fib(10) == 55
