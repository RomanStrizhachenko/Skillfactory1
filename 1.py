# TIC TAC toe game

TT = [None for _ in range(0, 9)] # список ходов игроков
N = ['Иванов', 1, 0, 1,'Петров', 0, 1] # список игроков
# [игрок1, крестики, количество побед, кто ходит, игрок2, количество побед игрока2, кто первый ходил]
XY = [0, 0] # координаты ввода
XY = [int(i) for i in XY]

def PTT(TT): # функция вывода на экран поля игры
    PTT = ['  0 1 2', '/', '0 ', TT[0], TT[1], TT[2], '/', '1 ', TT[3], TT[4], TT[5], '/', '2 ', TT[6], TT[7], TT[8]]
    PTT = [("- " if i is None else i) for i in PTT]
    print('\n'.join(''.join(PTT).split('/')))
    return PTT

def IN(N): # определяем список игроков
    N[0] = input("Введите имя игрока 1  ")
    N[4] = input("Введите имя игрока 2  ")
    print(N[0], ", Ваш ход первый, Вы играете крестиками")
    return N

def CHECK(inp, TT): # выясняем корректность ввода координат
    ch = []
    ch = inp.split()  # cписок координат

    if len(ch) < 2:
        print('Вы ввели менее двух координат')
        print("Ввести надо два числа от 0 до 2 включительно через пробел")
        print("Повторите ввод координат")
        return False
    else:
       if ch[1].isdigit() and ch[0].isdigit():
           ch = list(map(int, inp.split()))
           if ch[0] > 2 or ch[1] > 2:
               print('Вы ввели значение больше числа 2')
               print("Ввести надо два числа от 0 до 2 включительно через пробел")
               print("Повторите ввод координат")
               return False
           else:
               if len(ch) > 2:
                   print('Вы ввели больше двух значений, но игра приняла только первые два')
                   if TT[ch[0] + ch[1] * 3] is None:
                       return True
                   else:
                       print("Ввод не корректный, с этими координатами ячейка уже заполена")
                       print("Ввести надо два числа от 0 до 2 включительно через пробел")
                       print("Повторите ввод координат")
                       return False
               else:
                   if TT[ch[0] + ch[1] * 3] is None:
                       return True
                   else:
                       print("Ввод не корректный, с этими координатами ячейка уже заполены")
                       print("Ввести надо два числа от 0 до 2 включительно через пробел")
                       print("Повторите ввод координат")
                       return False

       else:
           print('Вы ввели не числовые значения')
           print("Ввести надо два числа от 0 до 2 включительно через пробел")
           print("Повторите ввод координат")
           return False


def INTT(): # вводим координаты
    if N[3]:
        print("Ваш ход ", N[0], ", введите две координаты через пробел 0, 1 или 2")
    else:
        print("Ваш ход ", N[4], ", введите две координаты через пробел 0, 1 или 2")
    inp = input()
    return inp

def WIN(XY, TT, N): # кто-то уже выиграл?
    if TT[XY[1]*3] == TT[XY[1]*3+1] == TT[XY[1]*3+2] != None or TT[XY[0]] == TT[XY[0]+3] ==TT[XY[0]+6] != None or TT[0] == TT[4] == TT[8] != None or TT[2] == TT[4] == TT[6] != None:
        return True
    else:
        return False

def REP(): # будем еще играть?
    print("Проверьте чтобы была включена русская раскадка клавиатуры")
    if input("Сыграем еще партию? да? ").strip().lower() == "да":
        return True
    else:
        return False

IN(N)

Stop_game = True
while Stop_game:
   TT = [None for _ in range(0, 9)]  # список ходов игроков
   N[1] = 1

   while None in TT:
       PTT(TT) # рисуем поле
       inp = INTT() # вводим координаты

       if not CHECK(inp, TT): # проверяем корректность ввода
          continue
       else:
          XY = list(map(int, inp.split()))  # cписок координат
          if N[1] == 1:
             TT[XY[0] + XY[1] * 3] = 'x '  # ставим в позицию "х"
             N[1] = 0  # следующий ход нолики
          else:
             TT[XY[0] + XY[1] * 3] = 'o '  # ставим в позицию "о"
             N[1] = 1  # следующий ход крестики

          if WIN(XY, TT, N): # проверка победы
             PTT(TT)
             if N[3]:
                print(N[0], ", Вы выиграли в этой игре! Поздавляю!")
                N[2] += 1
             else:
                print(N[4], ", Вы выиграли в этой игре! Поздавляю!")
                N[5] += 1
             print("СЧЕТ:", N[0], N[2], " : ", N[5], N[4])
             if REP():
                print("Отлично, играем дальше!")
                N[6] = N[3] = 0 if N[6] else 1 # передает ход другому игроку
                break
             else:
                Stop_game = False
                break
          else:
             N[3] = 0 if N[3] else 1 # передает ход другому игроку
       if None not in TT:
          print("В этот раз ничья.")
          if REP():
             print("Отлично, играем дальше!")
             N[6] = N[3] = 0 if N[6] else 1  # передает ход другому игроку
             break
          else:
             Stop_game = False
             break
       else:
          continue