from random import randint


class Node:
    """Nodes perform simple operations on all data fed by an axiom"""
    def __init__(self):
        self.function = 0  # ^ / * + -
        self.axiomsIn = []
        self.data = 0

    def create(self,axIn):
        # choose a random function
        self.function = randint(0, 4)
        self.axiomsIn = axIn
        self.data = 0
        return self

    def createInputNode(self, data):
        self.data = data

    def go(self):
        self.data = 0

        for axiom in self.axiomsIn:
            data = axiom.getData()

            # Order
            if self.function == 0:
                self.data ^= data

            # Divide
            if self.function == 1:
                self.data /= data

            # Multiply
            if self.function == 2:
                self.data *= data

            # Addition
            if self.function == 3:
                self.data += data

            # Subtraction
            if self.function == 4:
                self.data -= data
