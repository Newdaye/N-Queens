
class nQueen:
    def __init__(self, qAmt):
        self.qAmount = qAmt
        self.rows, self.cols = (qAmt, qAmt)
        #self.board = [["-"*self.cols]]*self.rows
        self.board = [["-" for x in range(self.cols)] for y in range(self.rows)]
        self.printFirstSolution = True
        self.displayAll = False
        self.solutions = 0

    def setQueens(self, qAmt):
        self.qAmount = qAmt

    def getQueens(self):
        return self.qAmount
    def setDisplayAllSolutions(self):
        self.printFirstSolution = False
        self.displayAll = True

    def printArray(self):
        print("===")
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()
        print("===")

    #Checks: Row, Col, Diagonals. Returns True if move can be made, else returns false if queen is atacking
    def validMove(self, row, col):
        for i in range(row):
            if self.board[i][col] == "Q":
                return False
        ## TODO Fix this god awful mess if I have time, does the jobs though... zip function maybe? 
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i = row + 1
        j = col + 1
        while i < len(self.board) and j < len(self.board):
            if self.board[i][j] == "Q":
                return False
            i += 1
            j += 1
        
        i = row + 1
        j = col - 1
        while i < len(self.board) and j >= len(self.board):
            if self.board[i][j] == "Q":
                return False
            i += 1
            j -= 1
        i = row - 1
        j = col + 1
        while i>=0 and j < len(self.board):
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True
    
    def printSolutions(self):
        print(self.solutions)
        

    #problem is solved here
    def solve(self, row):
        if row == len(self.board):
            self.solutions += 1
            if self.printFirstSolution == True:
                self.printArray()
                self.printFirstSolution = False
            if self.displayAll == True:
                self.printArray()

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
            print("Enter 0 for queens to exit!")
            userInput = int(input("How many queens?: "))
            #print(userInput)
            if userInput == 0:
                break
        except:
            print("Enter an integer!")

        uInput = input("Display all solutions(y/n)? ")

            

        nq = nQueen(userInput)
        if uInput == "y":
            nq.setDisplayAllSolutions()
        else:
            print("Displaying only first result.")

        nq.solve(0)
        nq.printSolutions()
