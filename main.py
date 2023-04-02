import random

#Создаем класс корабля
class Ship:
    def __init__(self, cells):
        self.cells = cells

#Создаем класс доски для игры
class Board:
    # Создаем двумерный список размером 6x6
    def __init__(self):
        self.grid = [['O' for i in range(6)] for j in range(6)]
        self.ships = []
        self.hits = []
        self.misses = []

    # Метод для добавления корабля на доску
    def add_ship(self, ship):
        # Для каждой ячейки корабля меняем значение символа в списке grid на "■"
        for cell in ship.cells:
            self.grid[cell[0]][cell[1]] = '■'
        # Добавляем корабль в список кораблей на доске
        self.ships.append(ship)

    # Метод для проверки попадания по кораблю
    def check_hit(self, cell):
        # Проверяем, что данной клетки еще не было в списке попаданий или промахов
        if cell in self.hits or cell in self.misses:
            raise ValueError("Вы не можете выстрелить в данное поле")
        # Если клетка принадлежит хотя бы одному из кораблей на доске, добавляем ее в список попаданий и возвращаем True
        if cell in [ship.cells for ship in self.ships]:
            self.hits.append(cell)
            return True
        # Иначе добавляем клетку в список промахов и возвращаем False
        else:
            self.misses.append(cell)
            return False

    # Метод для проверки окончания игры (когда все корабли на доске подбиты)
    def is_game_over(self):
        return all([cell in self.hits for ship in self.ships for cell in ship.cells])

    # Метод для отображения текущего состояния доски в консоли
    def display(self):
        print("   | 1 | 2 | 3 | 4 | 5 | 6|")
        for i in range(6):
            row = [str(i + 1)]
            for j in range(6):
                if (i, j) in self.misses:
                    row.append('T')   # "T" - символ промаха
                elif (i, j) in self.hits:
                    row.append('X')   # "X" - символ попадания
                else:
                    row.append(self.grid[i][j])
            print(' | '.join(row))    # Объединяем ячейки в строку с разделителем " | " и выводим на экран


#Создаем функцию "Генератор кораблей"
def generate_ships():
    # Создаем пустой список кораблей
    ships = []

    # Проверка, что заданные клетки для корабля находятся в допустимых пределах поля и не пересекаются с другими кораблями
    def is_valid_location(cells):
        for cell in cells:
            # Проверяем, что координаты клетки находятся в пределах поля 6x6
            if cell[0] < 0 or cell[0] > 5 or cell[1] < 0 or cell[1] > 5:
                return False
            # Проверяем, что клетка не соседствует с другим кораблем
            for ship in ships:
                for neighbor in [(cell[0] - 1, cell[1] - 1), (cell[0] - 1, cell[1]), (cell[0] - 1, cell[1] + 1),
                                 (cell[0], cell[1] - 1), (cell[0], cell[1] + 1),
                                 (cell[0] + 1, cell[1] - 1), (cell[0] + 1, cell[1]), (cell[0] + 1, cell[1] + 1)]:
                    if neighbor in ship.cells:
                        return False
        return True

    # Создаем один корабль из трех клеток
    while True:
        # Выбираем случайное направление корабля
        direction = random.choice(['горизонталь', 'вертикаль'])
        if direction == 'горизонталь':
            start_row = random.randint(0, 5)
            start_col = random.randint(0, 3)
            cells = [(start_row, start_col), (start_row, start_col + 1), (start_row, start_col + 2)]
        else:
            start_row = random.randint(0, 3)
            start_col = random.randint(0, 5)
            cells = [(start_row, start_col), (start_row + 1, start_col), (start_row + 2, start_col)]
        # Проверяем, что клетки корабля находятся в допустимом местоположении и не пересекаются с другими кораблями
        if is_valid_location(cells):
            break
    # Добавляем корабль в список кораблей
    ships.append(Ship(cells))

    # Создаем два корабля из двух клеток
    for i in range(2):
        while True:
            # Выбираем случайное направление корабля
            direction = random.choice(['горизонталь', 'вертикаль'])
            if direction == 'горизонталь':
                start_row = random.randint(0, 5)
                start_col = random.randint(0, 4)
                cells = [(start_row, start_col), (start_row, start_col + 1)]
            else:
                start_row = random.randint(0, 4)
                start_col = random.randint(0, 5)
                cells = [(start_row, start_col), (start_row + 1, start_col)]
            # Проверяем, что клетки корабля находятся в допустимом местоположении и не пересекаются с другими кораблями
            if is_valid_location(cells):
                break
        ships.append(Ship(cells))

    # Создаем четыре корабля из одной клетки
    for i in range(4):
        while True:
            cell = (random.randint(0, 5), random.randint(0, 5))
            # Проверяем, что клетки корабля находятся в допустимом местоположении и не пересекаются с другими кораблями
            if is_valid_location([cell]):
                break
        ships.append(Ship([cell]))

    return ships




def main():
    # Приветствие и создание досок для игрока и компьютера
    print("Добро пожаловать в Морской Бой!")
    player_board = Board()      # создание доски для игрока
    computer_board = Board()    # создание доски для компьютера

    # Генерация кораблей и их расстановка на доске для игрока и компьютера
    computer_moves = [(i, j) for i in range(6) for j in range(6)]
    ships = generate_ships()    # генерация кораблей
    for ship in ships:
        player_board.add_ship(ship)     # расстановка кораблей на доске игрока
    ships = generate_ships()
    for ship in ships:
        computer_board.add_ship(ship)   # расстановка кораблей на доске компьютера

    # Игровой цикл
    while True:
        # Вывод досок на экран
        print("\nВаша доска:")
        player_board.display()
        print("\nДоска компьютера:")
        computer_board.display()

        # Ход игрока
        print("\nКуда вы хотите выстрелить?")
        row = int(input("Row: "))
        col = int(input("Column: "))
        try:
            if player_board.check_hit((row - 1, col - 1)):
                print("Попадание!")
            else:
                print("Промах!")
        except ValueError as e:
            print(e)
            continue

        # Проверка окончания игры после хода игрока
        if player_board.is_game_over():
            print("Вы выиграли!")
            break

        # Ход компьютера
        print("\nКомпьютер ходит...")
        move = random.choice(computer_moves)
        computer_moves.remove(move)
        if computer_board.check_hit(move):
            print("Компьютер попал!")
        else:
            print("Компьютер промахнулся!")

        # Проверка окончания игры после хода компьютера
        if computer_board.is_game_over():
            print("Компьютер победил!")
            break


if __name__ == '__main__':
    main()
