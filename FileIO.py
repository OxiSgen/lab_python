from abc import ABC, abstractmethod
import pickle


class FileOutputInterface(ABC):
    @abstractmethod
    def do_output(self):
        pass

    def do_input(self, data):
        pass


class FileOutputPickle(FileOutputInterface):
    def do_output(self):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)

    def do_input(self, data):
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)


class FileOutputShelve(FileOutputInterface):
    def do_output(self, arg):
        pass

    def do_input(self, data):
        pass

