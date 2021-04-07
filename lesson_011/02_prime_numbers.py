# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик
#
# TODO Не нужно Комментировать код задания. Можно выключить
#  вывод результатов, закомментировав цикл, но класс должен
#  быть раскомментирован.

class PrimeNumbers:
    def __init__(self, n):
        self.max_n = n
        self.prime_numbers = []
        self.count = 0

    def __iter__(self):
        self.count = 1
        return self

    def get_prime_numbers(self):
        self.count += 1
        for prime in self.prime_numbers:
            if self.count % prime == 0:
                return False
        return True

    def __next__(self):
        while self.count < self.max_n:
            if self.get_prime_numbers():
                self.prime_numbers.append(self.count)
                return self.count
        else:
            raise StopIteration()


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)

#  после подтверждения части 1 преподователем, можно делать


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


def fun_number(number):
    number = str(number)
    lenght = len(number)
    if lenght < 2:
        return True
    if lenght % 2 == 0:
        bit_depth = int(lenght / 2)
        left = number[:bit_depth]
        right = number[bit_depth:]
        if left == right:
            return True
        else:
            return False
    else:
        bit_depht = int((lenght - 1) / 2)
        left = (number[:bit_depht])
        right = (number[bit_depht + 1:])
        list_left = list(left)
        list_right = list(right)
        list_left_d = map(int, list_left)
        list_right_d = map(int, list_right)
        sum_left = sum(list_left_d)
        sum_right = sum(list_right_d)
        if sum_left == sum_right:
            return True
        else:
            return False


def palindromic_number(number):
    number = str(number)
    lenght = len(number)
    bit_depht = int((lenght - 1) / 2)
    left = (number[:bit_depht])
    right = (number[bit_depht + 1:])
    list_left = list(left)
    list_right = list(right)
    list_right.reverse()
    if list_left == list_right:
        return True
    else:
        return False


def trimorphic_number(number):
    kub_namber = number ** 3
    number = str(number)
    kub_namber = str(kub_namber)
    lenght_kub = len(kub_namber)
    lenght = len(number)
    slic = lenght_kub - lenght
    if kub_namber[slic:] == number:
        return True
    else:
        return False


# for number in prime_numbers_generator(n=10000):
#     print(number)



# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


# for number in prime_numbers_generator(n=100000):
#     res = fun_number(number=number)
#     print(f'Number-> {number} Fun {res}')


# for number in prime_numbers_generator(n=100000):
#     if len(str(number)) < 3:
#         continue
#     res = palindromic_number(number=number)
#     print(f'Number-> {number} Palindromic {res}')


for number in prime_numbers_generator(n=10000):
    third_degree = number ** 3
    res = trimorphic_number(number=number)
    print(f'Number-> {number} third degree {third_degree} Trimorphic {res}')
