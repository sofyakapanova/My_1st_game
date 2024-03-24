from tkinter import*                    #запускаем графический интерфейс
from For_game import Hero               #импортируем героя из файла For_game
from For_game import Monster            #импортируем мрнстра из файла For_game

def pos(player, monster):               #чтоб программа знала что делать если монстр догнал героя
    if player.coord == monster.coord:   #если коорд-ты игрока = коорд-там монстра (если монстр догнал игрока)
        player.lifes -= 1               #то снимаем у игрока жизнь
        canva.delete('enemy')           #удаляем все объекты с тэгом enemy из окна игры
        monster = Monster(canva)        #возвращаем монстра даже если он догнал героя
        return monster                  #возвращаем монстра даже если он догнал героя
    else:                               #иначе
        return monster                  #возвращаем монстра даже если он не догнал героя

def butnormal():                                            #для проверки функционирования кнопок (при соприкосновении с краем поля)
    coords = canva.coords('hero')                           #коорд-ты = коорд-ты героя на холсте
    if coords[0] != 0 and butleft['state'] == DISABLED:     #если коорд-та верх лев угла героя по х дошла до левого края окна (до 0)
      butleft.config(state=NORMAL)                          #возвращаем кнопке способность действовать
      butleft.bind('<Button-1>', moveleft)                  #делаем так, чтоб кнопка "влево" работала при нажатии на нее левой ('<Button-1>') кнопкой мыши и выполняла moveleft
    if coords[1] != 0 and butup['state'] == DISABLED:       #если коорд-та верх лев угла героя по y дошла до левого края окна (до 0)
      butup.config(state=NORMAL)                            #возвращаем кнопке способность действовать
      butup.bind('<Button-1>', moveup)                      #делаем так, чтоб кнопка "вверх" работала при нажатии на нее левой ('<Button-1>') кнопкой мыши и выполняла moveup
    if coords[2] != 200 and butright['state'] == DISABLED:  #если коорд-та ниж прав угла героя по x дошла до правого края окна (до 200)
      butright.config(state=NORMAL)                         #возвращаем кнопке способность действовать
      butright.bind('<Button-1>', moveright)                #делаем так, чтоб кнопка "вправо" работала при нажатии на нее левой ('<Button-1>') кнопкой мыши и выполняла moveright
    if coords[3] != 200 and butdown['state'] == DISABLED:   #если коорд-та ниж прав угла героя по y дошла до правого края окна (до 200)
      butdown.config(state=NORMAL)                          #возвращаем кнопке способность действовать
      butdown.bind('<Button-1>', movedown)                  #делаем так, чтоб кнопка "вниз" работала при нажатии на нее левой ('<Button-1>') кнопкой мыши и выполняла movedown
    enemylist[0].move(hero.coord[0], hero.coord[1], canva)  #заставляем монстра преследовать героя
    enemy = pos(hero, enemylist[0])
    enemylist.clear()
    enemylist.append(enemy)
    lbl.config(text='игрок: {} \nжизни: {}\nместоположение: {}\nинвентарь: {}'.format(hero.name, hero.lifes, hero.coord, hero.loot))

def moveup(event):  #event чтоб работало только при нажатии на кнопку
    hero.move('up')
    coords = canva.coords('hero')
    canva.delete('hero')
    canva.create_rectangle(coords[0], coords[1]-20, coords[2], coords[3]-20, fill='blue', tags='hero')
    print(coords)
    butnormal()
    if coords[1] == 20:
       butup.config(state=DISABLED)
       butup.unbind('<Button-1>')

def moveright(event):       #event чтоб работало только при нажатии на кнопку
    hero.move('right')
    coords = canva.coords('hero')
    canva.delete('hero')
    canva.create_rectangle(coords[0]+20, coords[1], coords[2]+20, coords[3], fill='blue', tags='hero')
    print(coords)
    butnormal()
    if coords[2] == 180:
       butright.config(state=DISABLED)
       butright.unbind('<Button-1>')

def movedown(event):     #event чтоб работало только при нажатии на кнопку
    hero.move('down')
    coords = canva.coords('hero')
    canva.delete('hero')    #удаляем героя с холста
    canva.create_rectangle(coords[0], coords[1]+20, coords[2], coords[3]+20, fill='blue', tags='hero')
    print(coords)  #выводим коорд-ты героя
    butnormal()    #вызываем ф-цию проверки на нормальность
    if coords[3] == 180:
       butdown.config(state=DISABLED)
       butdown.unbind('<Button-1>')

def moveleft(event):     #event чтоб работало только при нажатии на кнопку
    hero.move('left')
    coords = canva.coords('hero')
    canva.delete('hero')
    canva.create_rectangle(coords[0]-20, coords[1], coords[2]-20, coords[3], fill='blue', tags='hero')
    print(coords)
    butnormal() #вызываем ф-цию проверки на нормальность
    if coords[0] == 20:
       butleft.config(state=DISABLED)
       butleft.unbind('<Button-1>')

hero = Hero('sofya')
root = Tk()                                                         #вызываем холст
root.title('первая игра')                                           #называем холст
root.geometry('400x400')                                            #задаем размеры холста в пикселях
canva = Canvas(root, width=200, height=200, bg='white')             #создаем игровое поле 200х200 пикселей с белым фоном
canva.pack()                                                        #чтоб поле появилось на холсте
enemy = Monster(canva)                                              #enemy = обьект класса Monster на холсте
enemylist = [enemy]
for i in range(1, 10):                                              #создаем игровое поле 10х10 клеток
   canva.create_line(20*i, 0, 20*i, 200, fill='black')              #создаем вертикальные черные линии
   canva.create_line(0, 20 * i, 200, 20 * i, fill='black')          #создаем горизонтальные черные линии
canva.create_rectangle(80, 80, 100, 100, fill='blue', tags='hero')  #создаем героя
butleft = Button(root, text='влево')                                #создаем кнопку 1)в окне 2)с текстом влево, которая будет выполнять butleft
butright = Button(root, text='вправо')                              #создаем кнопку 1)в окне 2)с текстом вправо, которая будет выполнять butright
butup = Button(root, text='вверх')                                  #создаем кнопку 1)в окне 2)с текстом вверх, которая будет выполнять butup
butdown = Button(root, text='вниз')                                 #создаем кнопку 1)в окне 2)с текстом вниз, которая будет выполнять butdown
lbl = Label(root, text='игрок: {} \nжизни: {}\nместоположение: {}\nинвентарь: {}'.format(hero.name, hero.lifes, hero.coord, hero.loot))
lbl.pack()                              #чтоб надписи появились на холсте
butleft.place(x=50, y=300)              #располагаем кнопку влево по координатам 50, 300
butright.place(x=120, y=300)            #располагаем кнопку вправо по координатам 50, 300
butup.place(x=190, y=300)               #располагаем кнопку вверх по координатам 50, 300
butdown.place(x=250, y=300)             #располагаем кнопку вниз по координатам 50, 300
butleft.bind('<Button-1>', moveleft)    #делаем так, чтоб кнопка "влево" работала при нажатии на нее левой ('<Button-1>') кнопкой мыши и выполняла moveleft
butright.bind('<Button-1>', moveright)  #делаем так, чтоб кнопка "вправо" работала при нажатии на нее левой ('<Button-1>') кнопкой мыши и выполняла moveright
butup.bind('<Button-1>', moveup)        #делаем так, чтоб кнопка "вверх" работала при нажатии на нее левой ('<Button-1>') кнопкой мыши и выполняла moveup
butdown.bind('<Button-1>', movedown)    #делаем так, чтоб кнопка "вниз" работала при нажатии на нее левой ('<Button-1>') кнопкой мыши и выполняла movedown


root.mainloop()
