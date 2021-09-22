from ConsoleIO import ConsoleIO as CI
from FileIO import FileOutputPickle, FileOutputShelve
from Stusent import Student as St
from Captain import Captain as Cap


class MenuCartoteka:
	def __init__(self, strategy=FileOutputPickle()):
		self.__cart = []
		self.__strategy = strategy

	def add(self):
		case = int(input("0 - Студент, 1  - Староста: \n"))
		student = St if 0 else Cap
		self.__cart.append(CI.do_input(student))

	def change(self):
		pass

	def print(self):
		for st in self.__cart:
			st.output()

	def file_read(self):
		self.__strategy.do_output(self.__cart)

	def file_write(self):
		self.__cart = self.__strategy.do_input()

	def clear(self):
		self.__cart.clear()

	@property
	def strategy(self):
		return self.__strategy

	@strategy.setter
	def strategy(self, strategy) -> None:
		self.__strategy = strategy

