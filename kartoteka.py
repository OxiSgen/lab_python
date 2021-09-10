from Stusent import Student as St
from Captain import Captain as Cap


class MenuCartoteka:
	def __init__(self):
		self.methods = [
			self.add,
			self.print,
			self.file_read,
			self.file_write,
			self.clear,
			self.change,
		]
		self.cartoteka = []

	def add(self):
		while True:
			case = int(input("0 - Студент, 1  - Староста: \n"))
			if case == 0:
				self.cartoteka.append(St("qwerty", "uiop", 10))
				break
			elif case == 1:
				self.cartoteka.append(Cap("adsfd", "fwerf", 22, 1000))
				break
			else:
				print("Введи уже что-то разумное..")

	def print(self):
		for st in self.cartoteka:
			st.do_input_output()

	def file_read(self):
		print("dnfdshfkj")

	def file_write(self):
		print("dnfdshfkj")

	def clear(self):
		self.cartoteka.clear()
		print("dnfdshfkj")

	def change(self):
		pass

