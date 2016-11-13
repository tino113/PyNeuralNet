

class Axiom:
    """Weighted Links which feed data between nodes"""

    def __init__(self):
        self.nodeFrom = 0
        self.nodeTo = 0
        self.weight = 0

    def create(self,nFrom,nTo,w):
        self.weight = w
        self.nodeFrom = nFrom
        self.nodeTo = nTo
        return self

    def getData(self):
        return self.nodeFrom.data() * self.weight
