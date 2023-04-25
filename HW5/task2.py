def task2_start():
    """
    Запускает решение первой программы
    :return: выводит результат программы в консоль
    """

    add_number1 = int(input("Введите первое слогаемое: "))
    add_number2 = int(input("Введите второе слогаемое: "))

    def recursion_sum(number1, number2):
        summa = number1
        if number2 == 0:
            return summa
        return recursion_sum(number1, number2 - 1) + 1

    print(f"сумма двух чисел {add_number1} и {add_number2} равна {recursion_sum(add_number1, add_number2)}")
