def div(*args):

    try:
        num1 = int(input("Введите первое чило "))
        num2 = int(input("Введите второе число "))
        res = num1 / num2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Неверное чило! Делить на ноль нельзя!"

    return res

    '''
    if num2 != 0:
        return num1 / num2
    else:
        print("Неверное число! Делить на ноль нельзя!")
    '''


print(f'result  {div()}')