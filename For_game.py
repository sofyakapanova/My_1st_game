class Hero:
    def __init__(self, name):
        self.name = name
        self.lifes = 3
        self.coord = [5, 5]
        self.loot = []

    def move(self, d):
        if d == 'right':
            self.coord[0] = self.coord[0] + 1
        elif d == 'left':
            self.coord[0] -= 1
        elif d == 'up':
            self.coord[1] -= 1
        else:
            self.coord[1] += 1

    def lost_life(self):
        self.lifes -= 1

    def get_life(self, n):
        self.lifes += n

    def add_items(self, item):
        self.loot.append(item)


class Monster:
    def __init__(self, canva):
        self.coord = [10, 2]       #координаты начальн. полож-я монстра
        canva.create_rectangle(20*self.coord[0] - 20, 20*self.coord[1] - 20, 20*self.coord[0], 20*self.coord[1], fill='red', tags='enemy') #создаем квадрат(монстра): 20*self.coord[0] коорд-та прав. ниж. угла монстра х, 20*self.coord[1] коорд-та прав. ниж. угла монстра у, 20*self.coord[0]-20 коорд-та лев. верх. угла монстра x (-20 т.к. прав.ниж. угол по х отличается от верх. лев. на 20 пикселей), 20*self.coord[1]-20 коорд-та лев. верх. угла монстра y(-20 т.к. прав.ниж. угол по y отличается от верх. лев. на 20 пикселей)

    def move(self, x, y, canva):
        dx = self.coord[0] - x     #находим расст-е меж игроком и монстром по х
        dy = self.coord[1] - y     #находим расст-е меж игроком и монстром по у
        d = max(abs(dx), abs(dy))  #находим макс. расстояние
        if d == abs(dx):
            if dx < 0:
                self.coord[0] += 1

            elif dx > 0:
                self.coord[0] -= 1
            else:
                if dy > 0:
                    self.coord[1] -= 1
                else:
                    self.coord[1] += 1
        else:
            if dy > 0:
                self.coord[1] -= 1
            else:
                self.coord[1] += 1
        canva.delete('enemy')
        canva.create_rectangle(20 * self.coord[0] - 20, 20 * self.coord[1] - 20, 20 * self.coord[0], 20 * self.coord[1],
                               fill='red', tags='enemy')
