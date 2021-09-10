from ConsoleIO import ConsoleIO, ConsoleOutput, ConsoleInput


class Student:
    def __init__(self, name, surname, age, strategy=ConsoleOutput()):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
        self.__strategy = strategy

    def do_input_output(self) -> None:
        self.__strategy.do_action(str(self))

    def __str__(self):
        return "Имя: {}, Фамилия: {}, Возраст: {}".format(self.__name, self.__surname, self.__age)
