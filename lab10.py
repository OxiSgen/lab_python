import os
import tempfile
import datetime


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()

    def write(self, text):
        with open(self.file_path, 'w') as f:
            f.write(text)

    def __add__(self, file):
        storage_path = os.path.join(tempfile.gettempdir(), 'tempfile_lab10')
        with open(storage_path, 'w') as tf:
            concat_file = File(storage_path)
            concat_file.write(self.read() + file.read())
        return File(storage_path)

    def __iter__(self):
        self.position = 0
        return self

    def __next__(self):
        with open(self.file_path, 'r') as f:
            f.seek(self.position)
            line = f.readline()
            if not line:
                self.position = 0
                raise StopIteration('EOF')
            self.position = f.tell()
            return line.strip('\n')

    def __str__(self):
        return self.file_path


def main():
    first = File('first')
    second = File('second')
    new_obj = first + second

    print(f"Lines of {new_obj}:\n")
    for line in new_obj:
        print(line)


if __name__ == '__main__':
    main()