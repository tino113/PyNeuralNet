from network import Network
from node.Factory import Factory as NodeFactory

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

testNet = Network(inputs, outputs).generate(4, 20, False, True)

testNet.draw(512,512)

testNet.print(True)
