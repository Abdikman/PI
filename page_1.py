
"""Задание 1"""
def greet():
    name = input()
    second_name = input()
    print(f"Hello {name} {second_name}")


"""Задача 2"""
def who_are_you_and_hello(text: str = "Please, input youe name:\n"):
    name = input(text)
    if name.isalpha() and name.istitle() and len(name) > 1:
        print(f"Hi, {name}")
    else:
        who_are_you_and_hello("This string does not contain a name\n")


"""Задача 3"""
def quarter(xcoord: int = 3, ycoord: int = 4):
    if xcoord > 0:
        if ycoord > 0:
            print("I четверть")
        else:
            print("II четверть")
    else:
        if ycoord < 0:
            print("III четверть")
        else:
            print("IV четверть")


"""Задача 4"""
def golden_ratio(i: int = 4, fib=None, count: int = 0):
    count += 1
    if fib is None:
        fib = [1, 1]

    if count == i:
        print(fib[-1]/fib[-2])
    else:
        fib.append(fib[-1]+fib[-2])
        golden_ratio(fib=fib, count=count)


"""Задача 5"""
def ask_password(count: int = 0, password: str = "password"):
    user_input = input("Input your password:\n")
    if count == 3:
        raise Exception("You have repeatedly tried to enter the password.")
    if user_input == password:
        print("Пароль принят")
    else:
        print("В доступе отказано")
        count += 1
        ask_password(count)


"""Задача 6"""
def take_large_banknotes(banknotes=None, large10=None):
    if banknotes is None:
        banknotes = [1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]
        large10 = []

    for i in banknotes:
        if i > 10:
            large10.append(i)
            print(i)

    return large10


"""Задача 7"""
def month_name(month: int = 0, language: str = "en"):
    list_month = {"en": ["January", "Febrary", "March", "April", "May", "June", "July", "August", "Semptember", "October", "November", "December"],
                  "ru": ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]}

    return list_month[language][month-1]


def main():
    # greet()
    # who_are_you_and_hello()
    # quarter()
    # golden_ratio()
    # ask_password()
    # take_large_banknotes()
    print(month_name())

if __name__ == "__main__":
    main()
