from time import sleep
from numpy.random import choice


class TicTacToe:

    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        # [0, 1, 2],
        # [3, 4, 5],
        # [6, 7, 8]

        self.player = 1
        self.ai = 2

        self.run = True

    # Checks if anyone has won yet.
    def check_winner(self):
        marks = []

        # Checking Horizontally
        for row in self.board:
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] == 1:
                    print("PLAYER WINS")
                    self.run = False
                    return None
                elif row[0] == 2:
                    print("AI WINS")
                    self.run = False
                    return None

        for row in self.board:
            for num in row:
                marks.append(num)

        # Checking Vertically

        n = 0
        for i in range(3):  # Go through every column
            if marks[n] == marks[n + 3] and marks[n + 3] == marks[n + 6]:
                if marks[n] == 1:
                    print("PLAYER WINS")
                    self.run = False
                    return None
                elif marks[n] == 2:
                    print("AI WINS")
                    self.run = False
                    return None
            n += 1

        # Checking Diagonally
        # Forward Slash /
        n = 0
        values = []
        for i in range(3):
            values.append(marks[n])
            n += 4
        if values[0] == values[1] and values[1] == values[2]:
            if values[0] == 1:
                print("PLAYER WINS")
                self.run = False
                return None
            elif values[0] == 2:
                print("AI WINS")
                self.run = False
                return None

        values.clear()

        # Backwards Slash \
        n = 2
        for i in range(3):
            values.append(marks[n])
            n += 2
        if values[0] == values[1] and values[1] == values[2]:
            if values[0] == 1:
                print("PLAYER WINS")
                self.run = False
                return None
            elif values[0] == 2:
                print("AI WINS")
                self.run = False
                return None

        # Checking if all spots are filled
        for row in self.board:
            for num in row:
                if num == 0:  # There is still an empty space, so keep running
                    return None

        print("Nobody wins! Draw!!")
        self.run = False
        return None

    # Draws a mark for the AI by assessing which spot has been taken and which has not
    def ai_draw(self):
        for row in self.board:
            for num in row:
                if num == 0:
                    if self.board.index(row) == 2 or self.board.index(row) == 1:
                        row_index = self.board.index(row)
                        num_index = row.index(num)
                        self.board[row_index][num_index] = self.ai
                        return None
                    else:
                        draw = choice([True, False], p=[0.4, 0.6])
                        if draw:
                            row_index = self.board.index(row)
                            num_index = row.index(num)
                            self.board[row_index][num_index] = self.ai
                            return None

    # Prints the whole board and converts the board 2D array into circles and 'X'es
    def print_board(self):
        marks_in_row = []
        # Firstly, we only go through the first two rows so we create a for loop that will loop twice.
        # Then in the for loop, we access the row of each loop, meaning we access the first row and then the second row
        # Then we convert the number in each tile of each row to a mark and add it to the marks we need to draw
        # And finally, we draw the first two rows(still nested in the first for loop), and draw marks according to the order in
        # the marks_in_row list and we clear it for the next row. The concept is the same fro the last row
        for i in range(2):
            for num in self.board[i]:  # Conversion
                if num == 0:
                    marks_in_row.append(" ")  # adding to list to draw the mark after conversion
                elif num == 1:
                    marks_in_row.append("o")
                elif num == 2:
                    marks_in_row.append("x")

            # Drawing Row
            print(f" {marks_in_row[0]} | {marks_in_row[1]} | {marks_in_row[2]} ")
            print("___|___|___")
            marks_in_row.clear()  # Clear our row for the next row!

        for num in self.board[2]:
            if num == 0:
                marks_in_row.append(" ")
            elif num == 1:
                marks_in_row.append("o")
            elif num == 2:
                marks_in_row.append("x")
        print(f" {marks_in_row[0]} | {marks_in_row[1]} | {marks_in_row[2]} ")
        print("   |   |   ")

    # Gets the player's input and evaluates the validity of the spot they request
    def get_mark(self):
        user_mark = input("Where would you like to place your mark?")

        try:
            mark = int(user_mark)
        except Exception as e:
            self.run = False
            if e is None:
                return "This spot has already been taken. "
            else:
                return e

        if mark <= 3:
            # 1st Row
            if self.board[0][mark - 1] == 0:
                # To convert these marks, decrease it by the first tile in each row of the board.
                self.board[0][mark - 1] = self.player
                return "Spot Marked"
        elif mark <= 6:
            # 2nd Row
            if self.board[1][mark - 4] == 0:
                self.board[1][mark - 4] = self.player
                return "Spot Marked"
        elif mark <= 9:
            # 3rd Row
            if self.board[2][mark - 7] == 0:
                self.board[2][mark - 7] = self.player
                return "Spot Marked"
        else:
            self.run = False
            return "Invalid spot or that spot has already been marked."


game = TicTacToe()
while game.run:
    game.check_winner()
    sleep(1)
    print(game.get_mark())
    game.ai_draw()
    sleep(1)
    game.print_board()
    game.check_winner()
