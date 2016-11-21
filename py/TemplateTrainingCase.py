from network import Network
from node.Factory import Factory as NodeFactory
from visualization import Visualization

# determines the fitness of a network
def fitness():
    pass

# converts data from a source into nodes for first abstraction layer
inputs = [
    NodeFactory.create(1),
    NodeFactory.create(1),
    NodeFactory.create(1)
]

# converts data from a abstraction layer into data
outputs = [
    NodeFactory.create(1),
    NodeFactory.create(1),
    NodeFactory.create(1)
]

testNetwork = Network(inputs, outputs).generate(4, 20, True)

testNetwork.print(True)

Visualization(inputs, outputs, testNetwork.abstractionLayers, testNetwork.axiomOutList).draw(512,512)
