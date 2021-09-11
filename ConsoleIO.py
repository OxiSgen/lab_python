from abc import ABC, abstractmethod


class ConsoleOutputInterface(ABC):
    @abstractmethod
    def do_output(self, arg):
        pass


class ConsoleOutput(ConsoleOutputInterface):
    def do_output(self, arg):
        print(arg.name_and_age())


class ConsoleOutputModify(ConsoleOutputInterface):
    def do_output(self, arg):
        print(arg)


class ConsoleInput:
    @staticmethod
    def do_input(field_name):
        return input(f'Введите { field_name }:')