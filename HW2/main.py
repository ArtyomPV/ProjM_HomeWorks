import random


# ----------task1-------------------------------------------------------
# Задача 10: На столе лежат n монеток.Некоторые из них лежат вверх решкой,
# а некоторые – гербом.Определите минимальное число монеток, которые
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и
# той же стороной.Выведите минимальное количество монет, которые нужно перевернуть


def coins_game():
    n = int(input("Введите количество монет:  "))
    count_heads = 0
    count_tail = 0

    for k in [random.randint(0, 1) for _ in range(n)]:
        if k > 0.5:
            count_heads += 1
        else:
            count_tail += 1
    if count_heads > count_tail:
        print(f'Нужно перевернуть {count_tail} монет')
    else:
        print(f'Нужно перевернуть {count_heads} монет')


coins_game()

# ----------task2-------------------------------------------------------
# Задача 12: Петя и Катя – брат и сестра.Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.Он задумывает два натуральных числа X
# и Y(X, Y≤1000), а Катя должна их отгадать.Для этого Петя делает две подсказки.Он называет сумму
# этих чисел S и их произведение P.Помогите Кате отгадать задуманные Петей числа.


def guess_two_numbers():
    summa = int(input("Введите сумму чисел:  "))
    multiply = int(input("Введите произведение чисел:  "))
    for i in range(summa):
        for j in range(multiply):
            if summa == i + j and multiply == i * j:
                print(f'загаданные числа {i} и {j}')
            else:
                print(f'подсказки не верны')


guess_two_numbers()


# ----------task3-------------------------------------------------------
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input("Введите число  "))
i = 0
while n > 0:
    print(2**i)
    i += 1
    n -= 1
