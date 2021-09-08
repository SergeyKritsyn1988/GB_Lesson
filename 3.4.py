def my_func(x, y):
    return 1 / x ** abs(y)
    #return x ** y
print(my_func(2, -3))




# Вариант без **
def my_func():
    x = float(input("Введите положительное число, возводимое в степень: "))
    y = float(input("Введите степень ввиде целого отрацельного числа: "))
    res = 1
    while (y<0):
        res*= x
        y += 1
    res = 1/res
    return res
print(f'Рузультат - {my_func()}')