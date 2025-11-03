class Change:

    def __init__(self, total, provided):
        self.total = total
        self.provided = provided
        self.denominations = [100, 50, 20, 10, 5, 1, .25, .1, .05, .01]
        self.change = self.calculate()


    def calculate(self):
        
        # Calculate total change and initialize list for pair values
        change_total = self.provided - self.total
        quantity_by_denomination = []
        
        if change_total > 0:
            # Iterate over the denominations and append pair values to list
            for i in range(len(self.denominations)):

                # floor divide to get values
                quantity = change_total // self.denominations[i]

                # Adjust current change total
                change_total -= self.denominations[i] * quantity

                # If our quantity is greater than 0 add it to the quantity list by denomination
                if quantity > 0:
                    quantity_by_denomination.append((self.denominations[i], quantity))

                # if our current change total is 0 we no longer need to iterate
                if change_total == 0:
                    break


        return quantity_by_denomination