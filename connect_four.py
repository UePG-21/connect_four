"""
1. two players red yellow take turns
2. four coins same connected, game ends; no longer play, also ends.
3. view board at any time
"""
import random


class Board:
    def __init__(self) -> None:
        self.board = [[0] * 7 for _ in range(6)]
        self.nexts = [-1] * 7

    def show(self) -> None:
        for i in range(6):
            print(self.board[i])

    def check(self) -> int:
        # check row
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == 0:
                    continue
                if (
                    self.board[i][j]
                    == self.board[i][j + 1]
                    == self.board[i][j + 2]
                    == self.board[i][j + 3]
                ):
                    return self.board[i][j]
        # check column
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == 0:
                    continue
                if (
                    self.board[i][j]
                    == self.board[i + 1][j]
                    == self.board[i + 2][j]
                    == self.board[i + 3][j]
                ):
                    return self.board[i][j]
        # check positive diagonal
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == 0:
                    continue
                if (
                    self.board[i][j]
                    == self.board[i + 1][j + 1]
                    == self.board[i + 2][j + 2]
                    == self.board[i + 3][j + 3]
                ):
                    return self.board[i][j]
        # check negative diagonal
        for i in range(3, 6):
            for j in range(4, 7):
                if self.board[i][j] == 0:
                    continue
                if (
                    self.board[i][j]
                    == self.board[i - 1][j - 1]
                    == self.board[i - 2][j - 2]
                    == self.board[i - 3][j - 3]
                ):
                    return self.board[i][j]
        # check full board
        for i in range(6):
            for j in range(7):
                if self.board[i][j]:
                    return 0
        return -1

    def get_coin(self, player: int, col: int) -> bool:
        if self.nexts[col] == -7:
            return False
        self.board[self.nexts[col]][col] = player
        self.nexts[col] -= 1
        return True


class Game:
    def __init__(self) -> None:
        self.board = Board()

    def place_coin(self, player: int, col: int) -> bool:
        valid = self.board.get_coin(player, col)
        return valid

    def report(self) -> bool:
        # show board
        self.board.show()
        # report game
        state = self.board.check()
        if state == 1:
            print("player 1 wins")
        elif state == 2:
            print("player 2 wins")
        elif state == -1:
            print("game ends, no winner")
        else:
            print("game continues")
            return True
        return False


if __name__ == "__main__":
    g = Game()

    while True:
        while True:
            valid = g.place_coin(1, random.choice(list(range(7))))
            if valid:
                break
        on_going = g.report()
        if not on_going:
            break
        while True:
            valid = g.place_coin(2, random.choice(list(range(7))))
            if valid:
                break
        on_going = g.report()
        if not on_going:
            break
