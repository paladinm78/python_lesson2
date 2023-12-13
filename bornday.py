PUSHKIN_BIRTH_YEAR = 1799
PUSHKIN_BIRTH_DATE = '6 июня'
input_year = int(input('Какой год рождения А.С Пушкина? '))
if input_year == PUSHKIN_BIRTH_YEAR:
    input_day = input('Какой день рождения А.С Пушкина? ')
    if input_day == PUSHKIN_BIRTH_DATE:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Не верный год рождения')