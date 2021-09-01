def person(name, surname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {surname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


person(
    name=input('Введите ваше имя: '),
    surname=input('Введите вашу фамилию: '),
    year_of_birth=input('Введите год рождения: '),
    city=input('Введите город проживания: '),
    email=input('email: '),
    phone=input('Введите ваш номер телефона: '),
)
