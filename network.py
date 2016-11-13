from abstractionLayer import AbstractionLayer

class Network:

    abstractionLayers = []
    inputNodes = []
    outputNodes = []

    # generates a new random network, max layers, max nodes per layer and max
    # axiom weighting can all be determined
    def generate(self,inputNodes,outputNodes,numAbstractions,numNodesPerLayer):
        self.inputLayer = inputNodes
        self.outputLayer = outputNodes
        for i in range(numAbstractions):
            aL = AbstractionLayer()
            if i > 0:
                self.abstractionLayers.append(aL.create(self.abstractionLayers[i-1].nodes))
            else:
                self.abstractionLayers.append(aL.create(self.inputLayer))

            for j in range(numNodesPerLayer):
                aL.addNewNode()
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


