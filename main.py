def main():
    # Приветствие и создание досок для игрока и компьютера
    print("Добро пожаловать в Морской Бой!")
    player_board = Board() # создание доски для игрока
    computer_board = Board() # создание доски для компьютера

    # Генерация кораблей и их расстановка на доске для игрока и компьютера
    computer_moves = [(i, j) for i in range(6) for j in range(6)]
    ships = generate_ships() # генерация кораблей
    for ship in ships:
        player_board.add_ship(ship) # расстановка кораблей на доске игрока
    ships = generate_ships()
    for ship in ships:
        computer_board.add_ship(ship) # расстановка кораблей на доске компьютера

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
