# Программа является векториной вопрос/ответ.
def Viktorina_strany():
    print('Привет, это игра - векторина. Сутью которой является ответить на вопросы векторниы.')
    print('Для начала игры нажмите: 1')
    print('Для завершения игры нажмите: 0')
    tenet = int(input())
    cout = 0 # переменная для подсчета правильных ответов
    p = 0 # Переменная для инициализации порядка
    sp_osnov = {'Россия':'Москва', 'Франция':'Париж','Япония':'Токио','Австрия':'Вена','Бельгия':'Брюссель','Великобритания':'Лондон','Германия':'Берлин','Ирландия':'Дублин','Лихтенштейн':'Вадуц','Монако':'Монако'}
    sp_dop = {'Москва ':'Россия', 'Париж ':'Франция','Токио ':'Япония','Вена ':'Австрия','Брюссель ':'Бельгия','Лондон ':'Великобритания','Берлин ':'Германия','Дублин ':'Ирландия','Вадуц ':'Лихтенштейн','Монако ':'Монако'}
    mass = []
    for b in sp_dop:
        mass.append(b)
    try:
        while tenet == 1:
            for a in sp_osnov:
                print('Введите сталицу страны',a,':\n')
                var = input()
                var = var.title()
                if var == mass[p]:
                    print('Поздравляю,вы назвали верно')
                    cout += 1
                    print('**********************************')
                    print('Кол-во очков: ',cout)
                else:
                    print('Ошибка, попробуйте снова')
                    tenet = int(input('Для начала игры: 1. \nДля завершения: 0\n'))
                p += 1
            if tenet == 1 :
                tenet = 1
            elif tenet != 1 and tenet != 0:
                print('Ошибка')
            else:
                tenet = 0
    except:
        cout += 1
        print('Поздравляю, вы прошли игру! ')
        print('**********************************')
        print('Ваш баланс очков:', cout)
        print('**********************************')
        print('Максимальный баланс очков:', len(mass) + 1)
Viktorina_strany()