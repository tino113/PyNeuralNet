
class Axiom:
    """Weighted Links which feed data between nodes"""

    def __init__(self, nodeFrom, nodeTo, weight):
        self.weight = weight
        self.nodeFrom = nodeFrom
        self.nodeTo = nodeTo

    def print(self):
        print("axiom: " + str(self) + " from: " + str(self.nodeFrom) + " to: " + str(self.nodeTo) + " weight: " + str(self.weight))

    def getData(self):
        return self.nodeFrom.data() * self.weight
