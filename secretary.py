documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "1111"}
]
directories = {
    "1": ["2207 876234", "11-2", "5455 028765"],
    "2": ["10006", "5400 028765", "5455 002299"],
    "3": []
}


def output_name(documents):
    number_documents = input("Введите номер документа ")
    for element in documents:
        if number_documents in element.values():
            return element["name"]
    return "Данного документа не существует"


# p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит

def output_list():
    for part in documents:
        try:
            print(part["type"], part["number"], part["name"])
        except KeyError:
            print(f'Ошибка! У документа № {part["number"]} отсутствует "name"')
    return "-"


# l – команда, которая выведет список всех документов

def call_shelf(directories):
    number_document = input("Введите номер документа ", )
    for shelf, numbers in directories.items():
        if number_document in numbers:
            return shelf
    return "Данного документа не существует"


# s – команда, которая спросит номер документа и выведет номер полки, на которой он находится

def add(documents, directories):
    number = input("Введите номер документа ", )
    a_type = input("Введите тип документа ", )
    name = input("Введите имя владельца ", )
    number_dir = input("Введите номер полки ", )
    new_dir = {"type": a_type, "number": number, "name": name}
    if number_dir in directories.keys():
        documents.append(new_dir)
        for direct, numb in directories.items():
            if number_dir == direct:
                numb.append(number)
    else:
        return "Документ невозможно создать на данной полке"
    return documents, directories


# a – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,имя владельца и
# номер полки, на котором он будет храниться.

def open_input():
    command = input("Введите команду ", )
    if command == "p":
        return output_name(documents)
    elif command == "l":
        return output_list()
    elif command == "s":
        return call_shelf(directories)
    elif command == "a":
        return add(documents, directories)
    else:
        return "Такой команды нет"


print(open_input())
