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
        self.axioms = []

    def print(self, verbose = False):
        print("AbstractionLayer: " + str(self))
        if verbose:
            for node in self.nodes:
                Logger(verbose).outputNode(node)
            print(self.axioms)
            for axiom in self.axioms:
                axiom.print()

    def create(self, prevLNodes):
        self.prevLayerNodes = prevLNodes
        return self

    # TODO: get this working.
    '''
    def addNode(self, nodeIn):
        axIn = nodeIn.axiomsIn
        node = NodeFactory.createType(nodeIn.type, nodeIn.data)

        for prevN in self.prevLayerNodes:
            ax = Axiom()
            axIn.append(ax.create(prevN, node, sigmoid(uniform(-1, 1))))

        node.assignAxioms(axIn)
        self.nodes.append(node)
        self.axioms.extend(axIn)
    '''

    def addNewNode(self):
        axIn = []
        node = NodeFactory.create()

        for prevN in self.prevLayerNodes:
            ax = Axiom()
            axIn.append(ax.create(prevN, node, sigmoid(uniform(-1, 1))))

        node.assignAxioms(axIn)
        self.nodes.append(node)
        self.axioms.extend(axIn)

    def removeNode(self, n):
        self.nodes.remove(n)

    def go(self):
        for node in self.nodes:
            node.go()

