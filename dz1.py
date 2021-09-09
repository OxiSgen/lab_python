from enum import Enum, unique
import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ex(self):
        self.ext = os.path.splitext(self.photo_file_name)[1]
        return self.ext


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "Car"
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def on_create(cls, row):
        return cls(row[1], row[3], row[5], row[2])


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "Truck"
        if body_whl == '':
            self.body_whl = [0, 0, 0]
        else:
            self.body_whl = list(map(float, body_whl.split('x')))
        self.body_width = self.body_whl[0]
        self.body_height = self.body_whl[1]
        self.body_length = self.body_whl[2]

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

    @classmethod
    def on_create(cls, row):
        return cls(row[1], row[3], row[5], row[4])


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "SpecMachine"
        self.extra = extra

    @classmethod
    def on_create(cls, row):
        return cls(row[1], row[3], row[5], row[6])


@unique
class CarType(Enum):
    car = Car
    truck = Truck
    spec_machine = SpecMachine


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        try:
            for row in reader:
                try:
                    car_type = row[0]
                    class_name = CarType[car_type].value
                    car_list.append(class_name.on_create(row))
                except (ValueError, KeyError):
                    pass
        except IndexError:
            pass
    return car_list

