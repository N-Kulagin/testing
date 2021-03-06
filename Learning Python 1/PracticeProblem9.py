"""
Задача: Дано целое число n. Выведите следующее за ним четное число.
При решении этой задачи нельзя использовать условную инструкцию if и циклы.
"""

n = int(input("Введите целое число: "))

remainder = n % 2  # Остаток от деления n на 2, каждое нечётное число n имеет вид n = 2k+1, каждое чётное - n = 2k + 0
print(f"Следующее чётное число: {n+2-remainder}")