def task1_start():
    """
    Запускает решение первой программы
    :return: выводит результат программы в консоль
    """

    number = int(input("Введите число: "))
    degree_number = int(input("Введите степень числа: "))

    def exponentiation(number, degree):
        """
        Функция возводит число number в степень degree
        :param number: число
        :param degree: степень числа
        :return: возвращает число возведенную в степень
        """
        if degree == 1:
            return number
        return exponentiation(number, degree-1) * number

    print(f"Возведение числа {number} в степень {degree_number} равно {exponentiation(number, degree_number)}")