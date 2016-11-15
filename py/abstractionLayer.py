from random import uniform

from axiom import Axiom
from node import Node

from mathFuncs import sigmoid


class AbstractionLayer:
    """Abstraction layers hold collections of nodes"""

    def __init__(self):
        self.nodes = []
        self.prevLayerNodes = []
        self.axiomList = []

    def print(self, verbose = False):
        print("AbstractionLayer: " + str(self))
        if verbose:
            for node in self.nodes:
                node.print()
            print(self.axiomList)
            for axiom in self.axiomList:
                axiom.print()

    def create(self, prevLNodes):
        self.prevLayerNodes = prevLNodes
        return self

    def addNewNode(self):
        axIn = []
        nd = Node()
        for prevN in self.prevLayerNodes:
            ax = Axiom()
            axIn.append(ax.create(prevN,nd,sigmoid(uniform(-1,1))))
        self.nodes.append(nd.create(axIn))
        self.axiomList.extend(axIn)

    def removeNode(self, n):
        self.nodes.remove(n)

    def go(self):
        for node in self.nodes:
            node.go()

