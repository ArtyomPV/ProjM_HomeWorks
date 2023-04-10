def count_character(number):
    """
    Вычисляет сумму всех разрядов числа
    :param number: любое нутральное число
    :return: Возвращает строку с суммой цифр разряда числа
    """
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    return f"сумма всех цифр числа = {summa}"


def find_cranes(s):
    """
    Считает, кто, из детей, сколько сделал корабликов
    :param s: сумма всех журавликов сколько сделали дети
    :return: строку с описанием кто, сколько сделал корабликов
    первое значение Сергей, второе Катя, третье значение Петя
    """
    # s = serega + petya + katya
    # petya = serega
    # katya = 2 * (petya + serega)
    serega = s//6
    petya = serega
    katya = 2 * (petya + serega)
    return f"{s} -> {serega} {katya} {petya}"


def find_happy_ticket(number):
    """
    определяет счастливый билет или нет
    :param number: шестизначное число
    :return:если сумма первых трех цифр равна сумме последних трех, то выводим yes, иначе no
    """
    if 99999 < number < 1000000:
        number1 = number//1000
        number2 = number%1000
        if count_character(number1) == count_character(number2):
            return f"{number} -> yes"
        else:
            return f"{number} -> no"


def haveChocolate(length, width, slices):
    """
    определяет сколько долек можно отломить за один разлом
    :param length: длина шоколадки
    :param width: ширина шоколадки
    :param slices: количество долек
    :return: если можно отломить количество долек за один раз, то выводит yes, иначе no
    """
    if slices//length or slices//width:
        return f"{length} {width} {slices} -> yes"
    else:
        return f"{length} {width} {slices} -> no"
