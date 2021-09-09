from kartoteka import menu_cartoteka

container = {
    1: "Добавить элемент",
    2: "Вывести элемент на экран",
    3: "Считать из файла",
    4: "Выгрузить в файл",
    5: "Очистить",
    6: "Редактировать"
}


def main():
    print("------------------------------")
    for i, item in container.items():
        print(i, ": ", item)
    print("------------------------------")
    return int(input())


if __name__ == '__main__':
    cartoteka = menu_cartoteka()
    try:
        while True:
            type(cartoteka.methods[main()-1]())
    except Exception as ex:
        print(ex, "\nbye")