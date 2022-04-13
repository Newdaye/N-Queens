
class nQueen:
    def __init__(self, qAmt):
        self.qAmount = qAmt

    def setQueens(self, qAmt):
        self.qAmount = qAmt




if __name__ == "__main__":
    while True:
        try:
            userInput = int(input("How many queens?: "))
            print(userInput)
            if userInput == 0:
                break
        except:
            print("Enter an integer!")