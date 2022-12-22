

#  1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#  Пример:
#  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Вариант 1 выводит набор произведений чисел от 1 до N
#  n = int(input('Input your namber: '))
#  count = 1
#  for i in range(1, n+1):
#      count *= i
#      print(count, end = "; ")

# Вариант 2 выводит 1 список произведений чисел от 1 до N
n = int(input('Input your namber: '))
count, list = 1, []
for i in range(1, n+1):
    count *= i
    list.append(count)
print(list)
    