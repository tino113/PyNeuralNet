from random import randint


class Node:
    """Nodes perform simple operations on all data fed by an axiom"""
    def __init__(self, data = 0):
        self.function = 0  # ^ / * + -
        self.axiomsIn = []
        self.data = data

    def print(self, verbose = False):
        allFuncs = ['^', '/', '*', '+', '-']
        print("Node: " + str(self) + " func: " + allFuncs[self.function] + " data: " + str(self.data))
        if verbose:
            print("Node: " + str(self) + " axioms:")
            for axiom in self.axiomsIn:
                axiom.print()

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
