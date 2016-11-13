from random import uniform

from axiom import Axiom
from node import Node

from py.mathFuncs import sigmoid


class AbstractionLayer:
    """Abstraction layers hold collections of nodes"""

    def __init__(self):
        self.nodes = []
        self.prevLayerNodes = []
        self.axiomList = []

    def create(self,prevLNodes):
        self.prevLayerNodes = prevLNodes
        self.nodes = []
        return self

    def addNewNode(self):
        axIn = []
        nd = Node()
        for prevN in self.prevLayerNodes:
            ax = Axiom()
            axIn.append(ax.create(prevN,nd,sigmoid(uniform(-1,1))))
        self.nodes.append(nd.create(axIn))
        self.axiomList.append(axIn)

    def removeNode(self,n):
        self.nodes.remove(n)

    def go(self):
        for node in self.nodes:
            node.go()

