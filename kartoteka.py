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
		print(Student().name)
		self.cartoteka.append(Student().name)
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


class Student:
	def __init__(self):
		self.name = "Lexa"
		self.age = 10


class Captain(Student):
	def sta(self):
		self.name = "nasten'ka"
