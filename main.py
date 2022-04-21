
from logging.config import valid_ident


class nQueen:
    def __init__(self, qAmt):
        self.qAmount = qAmt
        self.rows, self.cols = (qAmt, qAmt)
        #self.board = [["-"*self.cols]]*self.rows
        self.board = [["-" for x in range(self.cols)] for y in range(self.rows)]
        self.printFirstSolution = True
        self.solutions = 0

    def setQueens(self, qAmt):
        self.qAmount = qAmt

    def getQueens(self):
        return self.qAmount

    def printArray(self):
        for i in self.board:
            print(i)
            print()
    
    #Checks: Row, Col, Diagonals. Returns True if move can be made, else returns false if queen is atacking
    def validMove(self, row, col):
        for i in range(row):
            if self.board[i][col] == "Q":
                return False
        #for i in range(len(self.board)):
        #    if self.board[i][i] == "Q":
        #        return False
        # Check upper diagonal on right side
        for i, j in zip(range(row, -1, -1),range(col, self.qAmount, 1)):
            if self.board[i][j]=="Q":
                return False

	    # Check upper diagonal on left side 
        for i, j in zip(range(row, -1, -1),range(col, -1, -1)):
            if self.board[i][j]=="Q":
                return False
        #k = len(self.board) - 1
        #for i in range(len(self.board)):
         #   if self.board[i][k] == "Q":
         #       return False
        #    k = k - 1
        return True


    def printSolutions(self):
        print(self.solutions)
        

    #problem is solved here
    def solve(self, row):
        if row == len(self.board):
            self.solutions += 1
            return
        for i in range(len(self.board)):
            if self.validMove(row, i):
                self.board[row][i] = "Q"
                self.solve(row+1)
                #we back track here
                self.board[row][i] = "-"

        

            
if __name__ == "__main__":
    while True:
        try:
            userInput = int(input("How many queens?: "))
            #print(userInput)
            if userInput == 0:
                break
        except:
            print("Enter an integer!")
        nq = nQueen(userInput)
        nq.solve(0)
        nq.printSolutions()
