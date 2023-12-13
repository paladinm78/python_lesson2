PUSHKIN_BIRTH_YEAR = 1799
PUSHKIN_BIRTH_DATE = '6 июня'

input_year = None
while input_year != str(PUSHKIN_BIRTH_YEAR):
    input_year = input('Какой год рождения А.С Пушкина? ')

input_day = None
while input_day != PUSHKIN_BIRTH_DATE:
    input_day = input('Какой день рождения А.С Пушкина? ')

print('Верно')
