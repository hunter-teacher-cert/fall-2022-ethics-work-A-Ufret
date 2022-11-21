# FILENAME: gol.py
# First Last: Ashley Ufret
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

class gol(object):
    """ generated source for class Cgol """
    board = [None]*r
    rows = board.length
    cols = board[0].length
    i = 0
    j = 0

    @classmethod
    def printBoard(cls, board):
        """ generated source for method printBoard """
        rows = board.length
        cols = board[0].length
        i = 0
        while i < rows:
            while cls.j < cols:
                print board[i][cls.j] + " ",
                cls.j += 1
            print 
            i += 1

    @classmethod
    def setCell(cls, board, r, c, val):
        """ generated source for method setCell """
        board[r][c] = val

    @classmethod
    def countNeighbours(cls, board, r, c):
        """ generated source for method countNeighbours """
        count = 0
        i = r - 1
        while i < r + 2:
            while cls.j < c + 2:
                if i > -1 and i < board.length and not (r == i and c == j) and cls.j > -1 and cls.j < board[0].length and board[i][cls.j] == 'X':
                    count += 1
                cls.j += 1
            i += 1
        return count

    @classmethod
    def getNextGenCell(cls, board, r, c):
        """ generated source for method getNextGenCell """
        neighbors = cls.countNeighbours(board, r, c)
        if board[r][c] == 'X' and (neighbors == 2 or neighbors == 3):
            return 'X'
        if board[r][c] == '.' and neighbors == 3:
            return 'X'
        return '.'

    @classmethod
    def generateNextBoard(cls, board):
        """ generated source for method generateNextBoard """
        rows = board.length
        cols = board[0].length
        newBoard = [None]*rows
        i = 0
        while i < rows:
            while cls.j < cols:
                newBoard[i][cls.j] = getNextGenCell(board, i, j)
                cls.j += 1
            i += 1
        return newBoard

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        board = []
        board = createNewBoard(10, 10)
        cls.setCell(board, 0, 0, 'X')
        cls.setCell(board, 0, 2, 'X')
        cls.setCell(board, 1, 1, 'X')
        cls.setCell(board, 2, 0, 'X')
        print "Gen X:"
        cls.printBoard(board)
        print "--------------------------\n\n"
        print "Cell (1,1) has " + cls.countNeighbours(board, 1, 1) + " neighbors"
        print "Cell (1,1) has the new state of  " + cls.getNextGenCell(board, 1, 1) + " 	."
        board = generateNextBoard(board)
        print "Gen X+1:"
        cls.printBoard(board)
        print "--------------------------\n\n"
        board = generateNextBoard(board)
        print "Gen X+2:"
        cls.printBoard(board)
        print "--------------------------\n\n"
