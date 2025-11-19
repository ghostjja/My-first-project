i =(input('Выберите язык: Русский или Английский / Select language: Russian or English:'))

if  i == 'Русский' or i == 'Russian':
    a = int(input(' Сколько вам лет?: '))
    if a > 100:
        print('Вам не может быть больше 100 лет')
    elif a < 0:
        print('Возраст не может быть отрицательным')
    else:
        b = 100 - int(a)
        print(f'Вам осталось жить: {b} лет')
        exit()

if i == 'Английский' or i == 'English':
    e = int(input('How old are you?: '))
    if e > 100:
        print("You can't be more than 100 years old")
    elif e < 0:
        print('Age cannot be negative')
    else:
        c = 100 - int(e)
        print(f'You have time to live: {c} years')
    exit()

