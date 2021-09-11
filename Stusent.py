from ConsoleIO import ConsoleOutputInterface, ConsoleOutputModify, ConsoleOutput, ConsoleInput


class Student:
    def __init__(self, name, surname, age, output=ConsoleOutput()):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__output = output
        self.__input = ConsoleInput()

    @property
    def out(self):
        return self.__output

    @out.setter
    def out(self, output) -> None:
        self.__output = output

    def output(self):
        return self.__output.do_output(self)

    def name_and_age(self):
        return f'Имя: { self.__name }, Возраст: { self.__age }'

    def __str__(self):
        return "Имя: {}, Фамилия: {}, Возраст: {}".format(
            self.__name, self.__surname, self.__age
        )
