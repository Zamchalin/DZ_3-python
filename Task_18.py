# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
n = int(input("Введите пожалуйста количество элементов от 0 до 10: "))
list_1 = [randint(0,10) for i in range(n)]
print(list_1)
x = int(input("Введите пожалуйста число: "))
result = 0
for i in list_1:
    if abs(i - x) < abs( result - x):
        result = i
print(result)



# l = input()
# numbers = list(map(int, input().strip().split()))
# print(numbers)
# x = int(input().strip())

# res = numbers[0]
# for i in numbers:
#     if abs(i - x) < abs(res - x):
#         res = i

# print(res)