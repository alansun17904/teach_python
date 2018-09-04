from .context import Shop


def test_buy_things_from_shop():
    # TODO - There are errors in the test cases with plurals and floating-numbers.
    assert Shop.buy_things_from_shop('Apples', 10, 15) == "Your Apples cost 150."
    assert Shop.buy_things_from_shop('Oranges', 0, 10) == "Your Oranges cost 0."
    assert Shop.buy_things_from_shop('Kiwis', 5, 3.5) == "Your Kiwis cost 17."
    assert Shop.buy_things_from_shop('Chips', 7, 2.99) == "Your Chips cost 20."
    assert Shop.buy_things_from_shop('Soaps', 1, 20) == "Your Soaps cost 20."
    assert Shop.buy_things_from_shop('Books', 400, 1.5) == "Your Books cost 600."

