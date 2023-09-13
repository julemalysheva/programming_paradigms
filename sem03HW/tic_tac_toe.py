# Задача
# Написать игру в “Крестики-нолики”

from player import HumanPlayer, ComputerPlayer
from game import Game

def main():
    # Создаем игроков
    # Для смены варианта игрока закомментировать/раскомментировать нужного

    # player1 = HumanPlayer("Игрок 1", "X") #Вариант игры человека в консоли
    player1 = ComputerPlayer("Компьютер 1", "X") #Игрок - компьютер
    player2 = ComputerPlayer("Компьютер 2", "O") #Игрок - компьютер

    # Создаем игру
    game = Game(player1, player2) 

    # Запускаем игру
    game.play()

# Точка входа в программу
if __name__ == "__main__":
    main()