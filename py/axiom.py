

class Axiom:
    """Weighted Links which feed data between nodes"""

    def __init__(self):
        self.nodeFrom = 0
        self.nodeTo = 0
        self.weight = 0

    def print(self):
        print("axiom: " + str(self) + " from: " + str(self.nodeFrom) + " to: " + str(self.nodeTo) + " weight: " + str(self.weight))

    def create(self,nFrom,nTo,w):
        self.weight = w
        self.nodeFrom = nFrom
        self.nodeTo = nTo
        return self

    def changeWeight(self, w):
        self.weight = w

    def getData(self):
        return self.nodeFrom.data() * self.weight
