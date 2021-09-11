from Stusent import Student as St
from Captain import Captain as Cap
from ConsoleIO import ConsoleInput as CI
from FileIO import FileOutputPickle, FileOutputShelve


class MenuCartoteka:
	def __init__(self, strategy=FileOutputPickle()):
		self.__cart = []
		self.__strategy = strategy

	def add(self):
		while True:
			case = int(input("0 - Студент, 1  - Староста: \n"))
			name = CI().do_input("Имя")
			surname = CI().do_input("Фамилия")
			age = CI().do_input("Возраст")
			if case == 0:
				self.__cart.append(St(name, surname, age))
				break
			elif case == 1:
				grant = CI().do_input("Надбавка")
				self.__cart.append(Cap(name, surname, age, grant))
				break
			else:
				print("Введи уже что-то разумное..")

	def change(self):
		pass

	def print(self):
		# Strategy ?
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

