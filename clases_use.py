from collections import UserDict


class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Inputed data must be str!")

        self.value = value

    def __str__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone):
        self.name = name
        self.phones = []

        if phone and isinstance(phone, Phone):
            self.phones.append(phone)
        else:
            raise ValueError("Phone must br class Phone")

    def __str__(self):
        return f"{self.name}: {', '.join([str(i) for i in self.phones])}"

    def add_phone(self, phone: Phone):

        if phone and isinstance(phone, Phone):
            self.phones.append(phone)
        else:
            raise ValueError("Phone must br class Phone")


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __str__(self):
        return ";\n".join([f"{k}: {v}" for k, v in self.data.items()])

    def check_name(self, name:str):
        if name in self.data:
            return True

        # self.data[record.name.value] = record



if __name__ == '__main__':
    book = AddressBook()

    record1 = Record(Name("Тест1"), Phone("0960969696"))
    record1.add_phone(Phone("12345"))

    print("record1: ", record1)

    book.add_record(record1)

    record2 = Record(Name("Тест2"), Phone("987865421"))

    book.add_record(record2)

    print("AddressBook: ", book)


