#TicTacToe
class Player:
    def __init__(self):
        self.name = ''
        self.symbol = ''

    #setter method
    def setName(self, x):
        self.name = x

    #setter method
    def setSymbol(self, x):
        self.symbol = x

    #getter method
    def getName(self):
        return self.name

    #getter method
    def getSymbol(self):
        return self.symbol

class Canvas:
    def __init__(self):
        self.board = []
        for i in range(3):
            x = ['[ ]']*3
            self.board.append(x)

    def display(self):
        print()
        for i in range(len(self.board)):
            print()
            for j in range(len(self.board[i])):
                print(self.board[i][j], end= ' ')

        print()

    def clearBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] ='[ ]'


    def updateBoard(self, r, c, symbol):
        if r <0 or r >= len(self.board): #invalid row
            return False
        if c <0 or c >= len(self.board[r]): #invalid col
            return False
        if self.board[r][c] != '[ ]': #location not empty
            return False

        #all ok, update the board
        self.board[r][c] = '[' + symbol + ']'
        return True

    def isFullBoard(self):
        for i in range(len(self.board)):#3
            for j in range(len(self.board[i])):#3
                if self.board[i][j] == '[ ]': #compare with empty
                    return False
        return True

    #getter methods
    def getRows(self):
        return len(self.board)

    def getCols(self):
        return  len(self.board[0])

    def valueAtCoordinate(self, r, c):
        return  self.board[r][c][1] #'[X]' ---> 'X'

class TicTacToe:
    def __init__(self):
        self.players = []
        for i in range(2):
            self.players.append(Player())
        self.canvas = Canvas()

    #win rules
    def checkWins(self, symbol):
        r = self.canvas.getRows()
        c = self.canvas.getCols()

        #check for rows
        for i in range(r):
            v1 = self.canvas.valueAtCoordinate(i,0)
            v2 = self.canvas.valueAtCoordinate(i,1)
            v3 = self.canvas.valueAtCoordinate(i,2)
            if v1 == symbol and v2 == symbol and v3 == symbol:
                return True

        #check for cols
        for i in range(c):
            v1 = self.canvas.valueAtCoordinate(0, i)
            v2 = self.canvas.valueAtCoordinate(1, i)
            v3 = self.canvas.valueAtCoordinate(2, i)
            if v1 == symbol and v2 == symbol and v3 == symbol:
                return True

        #check for diagonal
        flag = 0
        for i in range(r):
            temp = self.canvas.valueAtCoordinate(i,i)
            if temp != symbol:
                flag = 1
                break
        if flag == 0:
            return  True


        #check for reverse diagonal
        flag = 0
        for i in range(r):
            temp = self.canvas.valueAtCoordinate(i,r-i-1)
            if temp != symbol:
                flag = 1
                break
        if flag == 0:
            return True


        return False

    def play(self):
        #setup player names and symbols
        symbols = ['X', 'O']
        for i in range(2):
            x = input('Enter name for player ' + str(i+1) + ' ')
            self.players[i].setName(x)
            self.players[i].setSymbol(symbols[i])
            print(x, 'your symbol is ', symbols[i])

        #setup board
        self.canvas.clearBoard()

        #local variable for temporary and logical purposes
        isDraw = True
        current = 0 #default


        #play
        self.canvas.display()
        while not self.canvas.isFullBoard():
            name = self.players[current].getName()
            sym = self.players[current].getSymbol()
            print(name , '(', sym, ') plays :')
            r = int(input('row coordinate (0-2) '))
            c = int(input('col coordinate (0-2) '))

            if self.canvas.updateBoard(r, c, sym):
                self.canvas.display()
                #check for win
                if self.checkWins(sym):
                    print(name, '(', sym,') WINS!!!!!')
                    isDraw = False
                    break

                #change the player
                current = (current+1) % len(self.players)
            else:
                print('Invalid Move by', name, ', kindly play again.')

        if isDraw:
            print('Game Draw!!!')

def main():
    t = TicTacToe()
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        t.play()
        ch = input('play again? ')

main()




