with open('new_file.txt', 'a') as file:
    while True:
        user_answ = input('Введите что-нибудь: ')
        file.write(user_answ + '\n')
        if not user_answ:
            break