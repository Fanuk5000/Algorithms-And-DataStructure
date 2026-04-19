class Student:
    def __init__(self, name, surname, average_mark, group):
        self.name = name
        self.surname = surname
        self.average_mark = average_mark
        self.group = group

    def get_info(self):
        return f"Name: {self.name}, Surname: {self.surname}, Average Mark: {self.average_mark}, Group: {self.group}"
