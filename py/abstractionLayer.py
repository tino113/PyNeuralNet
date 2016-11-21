from random import uniform

from axiom import Axiom
from node.Factory import Factory as NodeFactory
from Logger import Logger
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
                Logger(verbose).outputNode(node)
            print(self.axiomList)
            for axiom in self.axiomList:
                axiom.print()

    def create(self, prevLNodes):
        self.prevLayerNodes = prevLNodes
        return self

    def addNewNode(self):
        axIn = []
        node = NodeFactory.create()

        for prevN in self.prevLayerNodes:
            ax = Axiom(prevN, node, sigmoid(uniform(-1, 1)))
            axIn.append(ax)

        node.assignAxioms(axIn)
        self.nodes.append(node)
        self.axiomList.extend(axIn)

    def removeNode(self, n):
        self.nodes.remove(n)

    def go(self):
        for node in self.nodes:
            node.go()

