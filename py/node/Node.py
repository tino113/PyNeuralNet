
class Node:

    """Nodes perform simple operations on all data fed by an axiom"""
    def __init__(self, data = 0):
        self.axiomsIn = []
        self.data = data

    def assignAxioms(self, axioms):
        self.axiomsIn = axioms

    def process(self):
        # extract all the axiom data to an array
        data = map((lambda ax: ax.getData()), self.axiomsIn)

        # apply node function to all the values in the array of data
        self.data = reduce((lambda accumulator, each: self.compute(accumulator, each)), data)

        return self.data
