def count_subjects():
    try:
        # Информатика: 100(л) 50(пр) 20(лаб).
        mydict = {}
        with open("file_3.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')  # name = Информатика, stats = 100(л) 50(пр) 20(лаб).
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                """1. [i for i in stats if i == ' ' or ('0' <= i <= '9')] - Перебирает все элементы и берет только цифры
                        и пробелы(для разделения цифр: [' ', '1', '0', '0', ' ', '5', '0', ' ', '2', '0'])
                 2. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]) с помощью join объединяет
                        получившееся: _100_50_20  (где _ это пробел)
                 3. ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()
                        - делит по пробелам методом .split(): ['100', '50', '20']
                 4. map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split())
                        - с помощью map(int, ['100', '50', '20']) приводит все элементы списка к типу int
                 5. с помощью sum(['100', '50', '20']) суммирует все элементы списка """
                mydict[name] = name_sum
            print(f"{mydict}")  # вывод:{'Информатика': 170}
    except FileNotFoundError:
        return 'Файл не найден.'


count_subjects()