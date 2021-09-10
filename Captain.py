from Stusent import Student


class Captain(Student):
    def __init__(self, name, surname, age, grants):
        super().__init__(name, surname, age)
        self.__grants = grants

