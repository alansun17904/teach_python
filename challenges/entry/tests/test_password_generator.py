from challenges.entry.src.password_generator import Password


def test_password_generator():
    assert len(Password.generate_password()) == 10
    assert Password.generate_password()[0].isalpha()
    assert Password.generate_password()[1].isalpha()
    assert Password.generate_password()[2].isalpha()
    assert Password.generate_password()[3].isalpha()
    assert Password.generate_password()[4].isalpha()

    assert Password.generate_password()[5].isdigit()
    assert Password.generate_password()[6].isdigit()
    assert Password.generate_password()[7].isdigit()
    assert Password.generate_password()[8].isdigit()

    assert Password.generate_password()[9] in '!@#?/*'

    #Unique tester
    assert Password.generate_password()[:5] != Password.generate_password()[:5]
    assert Password.generate_password()[5:9] != Password.generate_password()[5:9]