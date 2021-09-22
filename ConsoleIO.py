from abc import ABC, abstractmethod


class IOInterface(ABC):
    @abstractmethod
    def do_output(self, arg):
        pass

    def do_input(self):
        pass


class ConsoleOutput(IOInterface):
    def do_output(self, arg):
        print(arg.name_and_age())

    def do_input(self):
        pass


class WebOutput(IOInterface):
    def do_output(self, arg):
        pass

    def do_input(self):
        pass