

class Axiom:
    """Weighted Links which feed data between nodes"""

    nodeFrom = 0
    nodeTo = 0
    weight = 0

    def create(self,nFrom,nTo,w):
        self.weight = w
        self.nodeFrom = nFrom
        self.nodeTo = nTo
        return self

    def getData(self):
        return nodeFrom.data() * weight
