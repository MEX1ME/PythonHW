# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# from random import randint

# numCoins = int(input("Укажите количество монет, лежащих на столе "))

# heads = 0
# tails = 0
# coins = []
# i = 0

# while i < numCoins: # заполняем список нулями и единицами. это будет россыть монет на столе. "1" - орлы, "0" - решки
#     coins.append(randint(0,1))
#     i += 1

# for i in coins:
#     if i == 1: heads+=1
#     else: tails +=1

# print(coins)

# if heads > tails:
#     print(f"Нужно перевернуть {tails} монеток")
# elif tails > heads:
#     print(f"Нужно перевернуть {heads} монеток")
# else:
#     print(f"Нужно перевернуть {tails} монеток")

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# import math

# print(
#     "Добрый день. Данная программа отгадает два целых числа, которые вы загадали, если вы правильно введете их сумму и их произведение"
# )
# sumNum = int(input("Введите сумму чисел "))
# prodNum = int(input("Введите произведение чисел "))
# limitNum = 1000

# diskrim = sumNum * sumNum - 4 * prodNum

# if diskrim < 0 or diskrim == 0:
#     print("не получается найти решение, введите другие числа")
# else:
#     num1 = int((sumNum + math.sqrt(diskrim)) / 2)
#     num2 = int((sumNum - math.sqrt(diskrim)) / 2)
#     if num1 + num2 == sumNum and num1 * num2 == prodNum:
#         if num1 <= limitNum and num2 <= limitNum:
#             print(f"Вы загадали числа {num1} и {num2}")
#         else:
#             print(f"Числа должны быть меньше 1000 по условию задачи")
#     else:
#         print("не получается найти решение, введите другие числа")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# num = int(input("Введите число, которое проверяем "))

# temp = 2
# i = 1
# while temp <= num:
#     print(f"{temp} - двойка в степени {i}")
#     temp = temp * 2
#     i += 1

# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

# num = float(input("Введите число "))
# sumDig = 0
# while num % 1 > 0:
#     num = num * 10

# while num > 0:
#     digit = num % 10
#     num = num // 10
#     sumDig = sumDig + digit

# print(int(sumDig))

# задача 3 необязательная

# Валентина прогуляла лекцию по математике.
# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью.
# Помогите ей (при помощи функции all_divisors(number), которую напишете сами).
# Постарайтесь найти самое оптимальное решение.
# Результат представьте в виде списка (не забудьте отсортировать по возрастанию).

# Долгое
# num = int(input("Введите положителльное целое число больше 0 "))
# if num <= 0 or num % 1 > 0:
#     print("Введите правильное число")
# else:
#     for i in range(1, num):
#         if num % i == 0:
#             print(i)

# Быстрее

# import math
# num = int(input("Введите положителльное целое число больше 0 "))

# div = []
# for i in range(1, int(math.sqrt(num)) + 1):
#     if num % i == 0:
#         div.append(i)
#         if i != num // i:
#             div.append(num // i)

# def bSort(nums):
#     trig = True
#     while trig:
#         trig = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 trig = True


# bSort(div)
# print(div)
