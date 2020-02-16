a = input("Введите комбинацию по типу '+ x y'")
oper = ["+", "-", "*", "/"]
assert a[0] in oper, "Not operator"


def calculate():
    try:
        for operator in a:
            if operator == "+":
                return int(a.split()[1]) + int(a.split()[2])
            elif operator == "-":
                return int(a.split()[1]) - int(a.split()[2])
            elif operator == "*":
                return int(a.split()[1]) * int(a.split()[2])
            elif operator == "/":
                return int(a.split()[1]) / int(a.split()[2])
                a.split[2] != 0
    except ZeroDivisionError:
        return "Ошибка! На ноль не делим"
    except ValueError:
        return "Ошибка! Введено не число"
    except IndexError:
        return "Ошибка! Введено неверное количество аргументов"


print(calculate())
