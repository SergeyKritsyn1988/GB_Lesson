def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или R для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'R':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма  {sum_res}')
    print(f'Ваша итоговая сумма {sum_res}')


my_sum()