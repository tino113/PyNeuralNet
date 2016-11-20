from random import uniform
from random import randint
from mathFuncs import sigmoid
from node.Factory import Factory as NodeFactory
from network import Network
from abstractionLayer import AbstractionLayer
from axiom import Axiom

class Evolution:

    def __init__(self, mutationChance = 0.01, maxChildren = 1):
        self.mutationChance = mutationChance
        self.maxChildren = maxChildren

    def mutation(self, network):
        if uniform(0,1) <= self.mutationChance:
            mutationType = randint(4)
            layer = network.abstractionLayers[randint(0, len(network.abstractionLayers))]

            if mutationType == ADDNODE:
                layer.addNewNode()

            elif mutationType == REMOVENODE:
                node = layer.nodes[randint(0, len(layer.nodes))]
                layer.removeNode(node)

            elif mutationType == CHANGEWEIGHT:
                numAxioms = len(layer.axioms)
                axiom = layer.axioms[randint(0, numAxioms)]
                axiom.changeWeight(sigmoid(uniform(-1, 1)))

            elif mutationType == CHANGEFUNCTION:
                nodeNum = randint(0, len(layer.nodes))
                layer.nodes[nodeNum] = NodeFactory.create(layer.nodes[nodeNum].data)

    def mitosis(self, network):
        networks = list(network)
        for child in range(randint(1, self.maxChildren)):
            networks.append(self.mutation(network))
        return networks

    def meiosis(self, networks):
        newNetworks = []
        nth = len(networks)
        inputs = networks[0].inputNodes  # inputs stay the same
        outputs = networks[0].outputNodes  # outputs stay the same
        maxNumLayers = len(max(networks.abstractionLayers, key=len))
        abstractionLayers = []

        for child in range(randint(1, self.maxChildren)):
            newNetworks.append(Network(inputs, outputs))

            for layerNum in range(0, maxNumLayers):
                aL = AbstractionLayer()
                # TODO: fix cases where networks have different numbers of abstractionLayers
                maxNumNodes = len(max([layer.nodes for layer in networks.abstractionLayers[layerNum]], key=len))

                if layerNum > 0:
                    abstractionLayers.append(aL.create(abstractionLayers[layerNum-1].nodes))
                else
                    abstractionLayers.append(aL.create(inputs))

                for j in range(maxNumNodes):
                    aL.addNewNode()

                for nodeNum in range(0, maxNumNodes):



        return newNetworks

    def reproduction(self, networks):

        if len(networks) == 0:
            print("Evolution: ERROR - Insufficient networks for reproduction, must have >=1 networks.")
        elif len(networks) == 1:  # mitosis
            return self.mitosis(networks[0])
        else:  # meiosis
            return self.meiosis(networks)

ADDNODE = 0

REMOVENODE = 1

CHANGEWEIGHT = 2

CHANGEFUNCTION = 3
