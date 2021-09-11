from Stusent import Student as St
from Captain import Captain as Cap
from ConsoleIO import ConsoleInput as CI


class MenuCartoteka:
	def __init__(self):
		self.cartoteka = []

	def add(self):
		while True:
			case = int(input("0 - Студент, 1  - Староста: \n"))
			name = CI().do_input("Имя")
			surname = CI().do_input("Фамилия")
			age = CI().do_input("Возраст")
			if case == 0:
				self.cartoteka.append(St(name, surname, age))
				break
			elif case == 1:
				grant = CI().do_input("Надбавка")
				self.cartoteka.append(Cap(name, surname, age, grant))
				break
			else:
				print("Введи уже что-то разумное..")

	def change(self):
		pass

	def print(self):
		# Strategy ?
		for st in self.cartoteka:
			st.output()

	def file_read(self):
		print("dnfdshfkj")

	def file_write(self):
		print("dnfdshfkj")

	def clear(self):
		self.cartoteka.clear()
		print("dnfdshfkj")

