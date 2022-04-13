import math
import random


class Calculator:

    @classmethod
    def improved(cls, vod):

        number = float(input('Ведите число если выбрали mod,!,arccos '))

        if vod == 'mod':
            print('Ответ: ', math.fabs(number))
        if vod == 'arccos':
            print('Ответ: ', math.acos(number))
        if vod == '!':
            print('Ответ: ', math.factorial(number))

    @classmethod
    def random(cls):
        print(random.randint(0, 100))

    @classmethod
    def ordinary(cls, vod):
        number_one = float(input('Ведите первое число '))
        number_two = float(input('Введите второе число:'))
        if vod == '^':
            print('Ответ: ', pow(number_one, number_two))
        elif vod == '+':
            print('Ответ: ', number_one + number_two)
        elif vod == '-':
            print('Ответ: ', number_one - number_two)
        elif vod == '*':
            print('Ответ: ', number_one * number_two)
        elif vod == '/':
            print('Ответ: ', number_one / number_two)
