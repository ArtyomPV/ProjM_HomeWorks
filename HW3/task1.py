# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

def task1_start():
    """
    Запускает решение задачи
    """
    size = int(input("Введите размер массива: "))
    numbers = [int(input("Введите число: ")) for _ in range(size)]
    show_array(numbers)
    find_count_number(numbers)


def show_array(numbers):
    """
    Выводит в консоль содержимое массива
    :param numbers: массив, который необходимо вывести в консоль
    :return:
    """
    print("Вывод массива: ")
    for number in numbers:
        print(number, end=" ")


def find_count_number(numbers):
    """
    Запрашивает у пользователя число, которое нужно определить сколько раз оно встречается в массиве
    :param numbers: массив в котором нужно определить количество повторов искомого числа
    :return: Выводит в консоль сколько раз встречалось введеное число
    """
    search_number = int(input("\nВведите число, для подсчета сколько раз оно встречается в массиве: "))
    counter = 0
    for number in numbers:
        if number == search_number:
            counter += 1
    print(f"-> {counter}")
    if counter > 0:
        print(f"число {search_number} встречается {counter} раз")
    else:
        print("Такого числа  в массиве нет")


