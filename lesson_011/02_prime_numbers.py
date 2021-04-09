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
# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number


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


def prime_numbers_generator(n, filter):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            if filter(str(number)):
                yield str(number)


def sum_numbers(number):
    return sum(map(int, number))


def fun_number(number):
    middle = len(number) // 2
    return sum_numbers(number[:middle]) == sum_numbers(number[-middle:])


def palindromic_number(number):
    lenght = len(number)
    bit_depht = int((lenght - 1) / 2)
    left = (number[:bit_depht])
    right = (number[bit_depht + 1:])
    list_left = list(left)
    list_right = list(right)
    list_right.reverse()
    if list_left == list_right:
        return number


def trimorphic_number(number):
    kub_namber = int(number) ** 3
    kub_namber = str(kub_namber)
    lenght_kub = len(kub_namber)
    lenght = len(number)
    slic = lenght_kub - lenght
    if kub_namber[slic:] == number:
        return number


for x in prime_numbers_generator(1000, fun_number):
    print(f'Fun numbers -> {x}')

for x in prime_numbers_generator(1000, palindromic_number):
    print(f'Palindromic -> {x}')

for x in prime_numbers_generator(1000, trimorphic_number):
    y = int(x) ** 3
    print(f'Trimorphic -> {x} ^3 -> {y}')
