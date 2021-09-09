class Student:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self, *args):
        return "Имя: {} Фамилия: {} Возраст: {}".format(self.__name, self.__surname, self.__age)
