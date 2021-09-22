from abc import ABC, abstractmethod


class IOInterface(ABC):
    @abstractmethod
    def do_output(self, arg):
        pass


class ConsoleIO(IOInterface):
    def do_output(self, arg):
        print(arg.name_and_age())

    @staticmethod
    def do_input(student_type):
        while True:
            print(student_type)
            name = input("Имя")
            surname = input("Фамилия")
            age = input("Возраст")
            '''            if case == 0:
                return student_type(name, surname, age)
            if case == 1:
                grant = input("Надбавка")
                return student_type(name, surname, age, grant)'''


class WebIO(IOInterface):
    def do_output(self, arg):
        pass

    @staticmethod
    def do_input(self, student_type):
        pass