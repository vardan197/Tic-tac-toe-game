class Board:

    sell_dict = {}

    def condition_of_board(self):
        row1_4_7_9 = f'     |     |     \n'
        row2 = f'  {self.sell_dict[1]}  |  {self.sell_dict[2]}  |  {self.sell_dict[3]}  \n'
        row3_6 = f'_____|_____|_____\n'
        row5 = f'  {self.sell_dict[4]}  |  {self.sell_dict[5]}  |  {self.sell_dict[6]}  \n'
        row8 = f'  {self.sell_dict[7]}  |  {self.sell_dict[8]}  |  {self.sell_dict[9]}  \n'
        board = row1_4_7_9 + row2 + row3_6 + row1_4_7_9 + row5 + row3_6 + row1_4_7_9 + row8 + row1_4_7_9
        print(board)

    def change_sell(self, sell_numb):
        if str(self.sell_dict[sell_numb]).isdigit():
            return True
        else:
            return False

    def check_end(self):
        if (self.sell_dict[1] == self.sell_dict[2] == self.sell_dict[3]) or\
           (self.sell_dict[4] == self.sell_dict[5] == self.sell_dict[6]) or\
           (self.sell_dict[7] == self.sell_dict[8] == self.sell_dict[9]) or\
           (self.sell_dict[1] == self.sell_dict[4] == self.sell_dict[7]) or\
           (self.sell_dict[2] == self.sell_dict[5] == self.sell_dict[8]) or\
           (self.sell_dict[3] == self.sell_dict[6] == self.sell_dict[9]) or\
           (self.sell_dict[1] == self.sell_dict[5] == self.sell_dict[9]) or\
           (self.sell_dict[3] == self.sell_dict[5] == self.sell_dict[7]):
            return True
        else:
            return False


class Player:
    def __init__(self, name, quantity_of_wins=0):
        self.name = name
        self.quantity_of_wins = quantity_of_wins

    def action(self, board, sell_value):
        while True:
            sell_numb = int(input(f'{self.name} введите номер клетки: '))

            try:
                if not 0 < sell_numb < 10:
                    raise ValueError('Номер клетки выходит за границы поля.')
                else:
                    if board.change_sell(sell_numb):
                        board.sell_dict[sell_numb] = sell_value
                        break
                    else:
                        print('Клетка с этим номером занята.')
            except ValueError as e:
                print(e)


class Game:

    moves_count = 0

    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.board = Board()

    def start_game(self):

        Board.sell_dict = {i_num: str(i_num) for i_num in range(1, 10)}

        while True:

            self.board.condition_of_board()
            self.player1.action(self.board, 'Х')
            self.moves_count += 1

            if self.board.check_end():
                print(f'{self.player1.name} победил!')
                self.board.condition_of_board()
                self.player1.quantity_of_wins += 1
                break

            self.board.condition_of_board()

            if self.moves_count == 9:
                print('Ничья!')
                break
            self.player2.action(self.board, 'О')
            self.moves_count += 1

            if self.board.check_end():
                print(f'{self.player2.name} победил!')
                self.board.condition_of_board()
                self.player2.quantity_of_wins += 1
                break


def main():
    print("Добро пожаловать в игру Крестики-нолики!")
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    game = Game(player1, player2)

    while True:
        game.start_game()
        print(f"Текущий счет: {game.player1.name} - {game.player1.quantity_of_wins},"
              f" {game.player2.name} - {game.player2.quantity_of_wins}"
              )
        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()

        if play_again.lower() != 'да':
            break


if __name__ == '__main__':
    main()