"""
Задача: Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого
из моментов времени. Известно, что второй момент времени наступил не раньше первого.
Определите, сколько секунд прошло между двумя моментами времени.

Входные данные
Программа на вход получает три целых числа — часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени.

Выходные данные
Выведите число секунд между этими моментами времени.
"""

hours, minutes, seconds = map(int,input("Введите часы, минуты, секунды через пробел: ").split())
time_1 = (hours,minutes,seconds)

hours, minutes, seconds = map(int,input("Введите часы, минуты, секунды через пробел: ").split())
time_2 = (hours,minutes,seconds)

if time_1 == time_2:
    print("Между моментами времени прошло 0 секунд.")
else:
    time_diff = (time_2[0]-time_1[0],time_2[1]-time_1[1],time_2[2]-time_1[2])
    seconds = time_diff[0] * (60**2) + time_diff[1] * 60 + time_diff[2]
    print(f"Между моментами времени прошло {seconds} секунд.")