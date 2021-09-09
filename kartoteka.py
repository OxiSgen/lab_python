from Stusent import Student as St
from Captain import Captain as Cap


class menu_cartoteka:
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
		case = int(input("0 - Студент, 1  - Староста"))
		if case == 0:
			pass
		elif case == 1:
			pass
		else:
			pass
		print(St().name)
		self.cartoteka.append(St().name)
		print("add")

	def print(self):
		print(self.cartoteka)
		print("print")

	def file_read(self):
		print("dnfdshfkj")

	def file_write(self):
		print("dnfdshfkj")

	def clear(self):
		self.cartoteka.clear()
		print("dnfdshfkj")

	def change(self):
		pass

