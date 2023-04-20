from HW3.task1 import show_array


def task2_start():
    print("Если желаете ввести значения сами нажмите - 1,")
    print("Если желаете использовать  значения  программы нажмите - 2.")
    option = int(input())
    match(option):
        case 1:
            size = int(input("Введите размер массива: "))
            numbers = [int(input("Введите число: ")) for _ in range(size)]
            show_array(numbers)
            number = int(input("\nВведите число: "))
            find_closest_element(number, numbers)
        case 2:
            number = 15
            numbers = [3, 2, 8, 12, 7, 1]
            show_array(numbers)
            print("\nЗаданное число", number)
            find_closest_element(number, numbers)


def find_closest_element(number, numbers):
    """

    :param number: число которое необходимо найти или ближайшее число к нему
    :param numbers: массив в котором ищем число или ближайшее число к нему
    :return: запрошенное число или самое близкое к нему с большей или меньшей стороны
    """
    # max = numbers[0]
    less_closest_index = 0
    # more_closest_index = len(numbers) - 1
    more_closest_index = 0
    flag = True
    for i in range(len(numbers)):
        if numbers[i] < number:
            if numbers[less_closest_index] < numbers[i]:
                less_closest_index = i
        n = numbers[i]
        if numbers[i] > number:
            if flag:
                more_closest_index = i
                flag = False
            if numbers[more_closest_index] > numbers[i]:
                more_closest_index = i
    print("Самый близкий по величине элемент к заданному числу")
    if flag:
        print(numbers[less_closest_index])
    else:
        if number - numbers[less_closest_index] <= numbers[more_closest_index] - number:
                    print(numbers[less_closest_index])
        if number - numbers[less_closest_index] > numbers[more_closest_index] - number:
                    print(numbers[more_closest_index])


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6

#     -> 5
