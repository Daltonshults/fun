class Change:

    def __init__(self, total, provided):

        self.total = total
        self.provided = provided
        self.denominations = [100, 50, 20, 10, 5, 2, 1, .25, .1, .05, .01]


    def calculate(self):
        for i in range(len(self.denominations)):
            change = 0
            print(self.denominations[i])
        


change = Change(15.00, 17.00)

change.calculate()