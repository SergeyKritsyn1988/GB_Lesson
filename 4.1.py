def salary_calculation():
    try:
        time = float(input('Выработка в часах: '))
        salary = float(input('Ставка в час в рублях: '))
        bonus = float(input('Премия в рублях: '))
        result = time * salary + bonus
        print(f'Заработная плата сотрудника  {result}')
    except ValueError:
        return print('введите числовое значение')
salary_calculation()