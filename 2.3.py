number = int(input("Веедите номер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентябрь',
                  10: 'Октябрь',
                  11: 'Ноябрь',
                  12: 'Декабрь'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Month from list is {month_list[i]}")
            break
    print(f"Month from dict is {month_dict[number]}")
else:
    print("Ошибка, введите от 1 до 12")