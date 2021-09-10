from abc import ABC, abstractmethod
from typing import List


class ConsoleIO(ABC):
    @abstractmethod
    def do_action(self, data):
        pass


class ConsoleInput(ConsoleIO):
    def do_action(self):
        input()


class ConsoleOutput(ConsoleIO):
    def do_action(self, arg):
        print(arg)
