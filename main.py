
class nQueen:
    def __init__(self, qAmt):
        self.qAmount = qAmt
        self.rows, self.cols = (qAmt, qAmt)
        self.board = [["-"*self.cols]]*self.rows

    def setQueens(self, qAmt):
        self.qAmount = qAmt
    
    def getQueens(self):
        return self.qAmount

    def printArray(self):
        for i in self.board:
            for j in i:
                print(j, end = " ")
            print()
    
    #Checks: Row, Col, Diagonals. Returns True if move can be made, else returns false if queen is atacking
    def validMove(self):
        pass
    

if __name__ == "__main__":
    while True:
        try:
            userInput = int(input("How many queens?: "))
            print(userInput)
            if userInput == 0:
                break
        except:
            print("Enter an integer!")
        else:
            nq = nQueen(userInput)
            nq.printArray()
