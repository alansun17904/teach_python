class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def give_raise(self, percent):
        self.pay = self.pay*(1 + percent)
        return

    def last_name(self):
        # TODO: implement this method!
        return


class Manager(Person):
    # TODO: implement this class!
    def __init__(self, name, job='Manager', pay=100):
        super().__init__(name, job, pay)

    def give_raise(self, percent, bonus=.1):
        # TODO: implement this method!
        return
