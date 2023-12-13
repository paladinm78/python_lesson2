BIRTH_YEAR_ALEKSANDR_PUSHKIN = 1799     # Год рождения Александра Пушкина
BIRTH_YEAR_LEV_TOLSTOY = 1828           # Год рождения Льва Толстого
BIRTH_YEAR_FEDOR_DOSTOEVSKY = 1821      # Год рождения Федора Достоевского
BIRTH_YEAR_ANTON_CHEKHOV = 1860         # Год рождения Антона Чехова
BIRTH_YEAR_NIKOLAY_GOGOL = 1809         # Год рождения Николая Гоголя

continue_game = True
while continue_game:
    correct_answers = 0
    input_year = input('Укажите год рождения Александра Пушкина: ')
    if input_year == str( BIRTH_YEAR_ALEKSANDR_PUSHKIN):                # 1799
        correct_answers += 1

    input_year = input('Укажите год рождения Льва Толстого: ')
    if input_year == str( BIRTH_YEAR_LEV_TOLSTOY):                      # 1828
        correct_answers += 1

    input_year = input('Укажите год рождения Федора Достоевского: ')
    if input_year == str( BIRTH_YEAR_FEDOR_DOSTOEVSKY):                 # 1821
        correct_answers += 1

    input_year = input('Укажите год рождения Антона Чехова: ')
    if input_year == str( BIRTH_YEAR_ANTON_CHEKHOV):                    # 1860
        correct_answers += 1

    input_year = input('Укажите год рождения Николая Гоголя: ')
    if input_year == str(BIRTH_YEAR_NIKOLAY_GOGOL):                     # 1809
        correct_answers += 1

    questions_count = 5
    incorrect_answers = questions_count - correct_answers
    correct_percent = 100 * correct_answers / questions_count
    incorrect_percent = 100 * incorrect_answers / questions_count

    print('Правильных ответов: ', correct_answers)
    print('Неправильных ответов: ', incorrect_answers)
    print(f'Процент правильных ответов {correct_percent}%')
    print(f'Процент неправильных ответов {incorrect_percent}%')

    continue_answer = None
    while not (continue_answer == 'да' or continue_answer == 'нет'):
        continue_answer = input('Хотите ли вы продолжить игру? (да/нет) ')
    if continue_answer == 'нет':
        continue_game = False
