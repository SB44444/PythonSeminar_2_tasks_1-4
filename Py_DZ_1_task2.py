#  2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1. 
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

n = int(input('Введите Ваше число: '))
for i in range(2, n):  # Цикл перебирает i в интервале от 2 до N-1
    if n % i == 0:
        print(f' Число {i} наименьший натуральный делитель целого числа N')
        break    
else:
    print(f'Число {n} простое и делится без остатка тоько на 1 и само себя')       
