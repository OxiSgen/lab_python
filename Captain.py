from Stusent import Student


class Captain(Student):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def __str__(self, *args):
        super(args)
