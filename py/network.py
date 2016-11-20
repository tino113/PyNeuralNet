from abstractionLayer import AbstractionLayer
from random import randint
from axiom import Axiom
from mathFuncs import sigmoid
from random import uniform
from visualization import Visualization

class Network:

    def __init__(self, inputs, outputs):
        self.abstractionLayers = []
        self.inputNodes = inputs
        self.outputNodes = outputs
        self.axiomOutList = []
        self.vis = Visualization(inputs, outputs, self.abstractionLayers, self.axiomOutList)

    def print(self, verbose = False):
        print("Network: " + str(self))
        if verbose:
            for aL in self.abstractionLayers:
                aL.print(True)

    def draw(self,w=256,h=256):
        self.vis.draw(w,h)

    # generates a new random network, max layers, max nodes per layer and max
    # axiom weighting can all be determined
    def generate(self, nLayers, numNodesPerLayer, nodesPerLayerMax = False):
        for i in range(nLayers):
            aL = AbstractionLayer()
            if i > 0:
                self.abstractionLayers.append(aL.create(self.abstractionLayers[i-1].nodes))
            else:
                self.abstractionLayers.append(aL.create(self.inputNodes))

            if nodesPerLayerMax:
                numNodesPerLayer = randint(len(self.outputNodes), numNodesPerLayer) # ensures diminishing tree to the right

            for j in range(numNodesPerLayer):
                aL.addNewNode()

        for outNode in self.outputNodes:
            axOut = []
            for prevN in self.abstractionLayers[-1].nodes:
                ax = Axiom()
                axOut.append(ax.create(prevN,outNode,sigmoid(uniform(-1,1))))
            self.axiomOutList.extend(axOut)

        return self

    def go(self):
        for aL in self.abstractionLayers:
            aL.go()

    # on a new birth there is a small chance of mutation of axiom weights,
    # a smaller chance of creating a new node in an existing abstraction layer,
    # and an even smaller chance of creating an entirely new abstraction layer.
    def mutate(self):
        pass

    # can be asexual or sexual, random weighting is used to determine the amount
    # of genetic data shared between parents, may contain 1 to n partners
    # N.B. Not limited to 1 or 2 partners
    def reproduce(self):
        pass


