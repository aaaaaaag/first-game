import random
N = int(input("Сколько игроков?: "))
k = N + 1
win = 0
summ = []
for i in range(0, k):
    summ.append(0)

while (win == 0):
    for i in range(1, k):
        rez = 'y'
        print("Ход игрока №", format(i))
        print("Сумма очков равна", format(summ[i]))
        number = random.randint(2,6)
        print ("Число ", format(number))
        sumprom = number
        print ("Выигрыш ", format(sumprom))
        while (rez != 'n'):
            rez = 'y'
            rez = input("Продолжаем y или n: " )
            if (rez == 'y'):
                number = random.randint(1, 6)
                if (number != 1):
                    sumprom += number
                    print ("Число ", format(number))
                    print ("Выигрыш ", format(sumprom))
                else:
                    print ("Попущен, выпала единица ГАГАГА :)))))")
                    sumprom = 0
                    rez = 'L'
                    break
        summ[i] += sumprom
        print("Сумма очков равна", format(summ[i]))
        if (summ[i] >= 10):
            win = 1
print ("Победил игрок №", format(i))