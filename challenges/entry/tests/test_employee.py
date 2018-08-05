from challenges.entry.src.employee import Person, Manager


def test_person():
    james = Person('James Smith',job='Engineer',pay=10)
    michael = Person('Michael Davis',job='Cashier',pay=15)
    john = Person('John Doe',job='Teacher',pay=20)

    # Attribute Tests
    assert john.name == 'John Doe'
    assert james.name == 'James Smith'
    assert michael.name == 'Michael Davis'

    assert james.job == 'Engineer'
    assert michael.job == 'Cashier'
    assert john.job == 'Teacher'

    assert james.give_raise(0.1) == 11.
    assert james.give_raise(0.5) == 16.5


def test_manager():
    james = Person('James Smith', job='Engineer', pay=10)
    michael = Manager('Michael Davis')

    assert michael.job == 'Manager'
    assert michael.pay == 100

    assert michael.give_raise(0.3, bonus=0.2) == 150
    assert michael.give_raise(0.5, bonus=0.0) == 225

    assert james.job == 'Engineer'
    assert james.last_name() == 'Smith'
