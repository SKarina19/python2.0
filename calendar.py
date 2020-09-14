# -*- coding: utf-8 -*-
from time import sleep


class Year(object):
    def __init__(self, date):
        self.date = date

    def leap_detect(self):
        if self.date % 4 != 0 or (self.date % 100 == 0 and self.date % 400 != 0):
            return True
        return False


class Month(Year):
    def __init__(self, date, month):
        self.month = month.lower()
        super().__init__(date)

    def show_holidays(self, flag):
        if flag:
            with open(str(self.month) + '.txt', "r+", encoding="utf-8") as f:
                s = f.read()
            print(s)
        elif not flag:
            with open(str(self.month) + "1" + '.txt', "r+", encoding="utf-8") as f:
                s = f.read()
            print(s)
        else:
            print("Неверный ввод месяца")

    def new_holidays(self, flag, new_str):
        if flag:
            with open(str(self.month) + '.txt', "r+", encoding="utf-8") as f:
                f.seek(0,2)
                #f.close()
                f.write("\n" + new_str )
        elif not flag:
            with open(str(self.month) + "1" + '.txt', "r+", encoding="utf-8") as f:
                f.seek(0,2)
                f.write("\n" + new_str)
                #f.close()
        else:
            print("Неверный ввод месяца")


def menu():
    print('┌', " Меню ".center(51, '—'), '┐', sep='')
    print("│ •1 Добавить праздник в календарь                  │")
    print("│ •2 Вывести все праздники за месяц                 │")
    print("│ •9 Вывести меню                                   │")
    print("│ •0 Выход                                          │")
    print('└', '—' * 51, '┘', sep='')


def wtopa():
    menu()
    while True:
        try:
            try:
                p = int(input('Введите номер пункта: '))
            except ValueError:
                print("Введите цифру")
                continue
            if p == 1:
                year = int(input("Введите год - "))
                date = Month(year, input("Введите месяц (в формате: сентябрь)- "))
                flag = date.leap_detect()
                new_str = input("Введите праздник")
                date.new_holidays(flag, new_str)
            elif p == 2:
                year = int(input("Введите год - "))
                date = Month(year, input("Введите месяц (в формате: сентябрь)- "))
                flag = date.leap_detect()
                date.show_holidays(flag)
            elif p == 9:
                menu()
            elif p == 0:
                print("Выход из программы", end='')
                sleep(0.3)
                for j in range(3):
                    print('.', end='')
                    sleep(0.25)
                return
            else:
                print("Нет такого пункта меню!\n")
                sleep(1)
        except Exception as e:
            print('Ошибка: ', e)


wtopa()
