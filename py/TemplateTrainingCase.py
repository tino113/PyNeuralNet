from network import Network
from node.Factory import Factory as NodeFactory

# determines the fitness of a network
def fitness():
    pass

# converts data from a source into nodes for first abstraction layer
def inputData():
    return [
        NodeFactory.create(1),
        NodeFactory.create(1),
        NodeFactory.create(1)
    ]

# converts data from a abstraction layer into data
def outputData():
    return [
        NodeFactory.create(1),
        NodeFactory.create(1),
        NodeFactory.create(1)
    ]

inputs = inputData()
outputs = outputData()

testNet = Network().generate(inputs,outputs,4,20,False,True)
testNet.draw(512,512)

testNet.print(True)
