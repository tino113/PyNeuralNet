from network import Network
from node import Node


# determines the fitness of a network
def fitness():
    pass

# converts data from a source into nodes for first abstraction layer
def inputData():
    nd = Node()
    nd.data = 1
    nd1 = Node()
    nd1.data = 1
    nd2 = Node()
    nd2.data = 1
    result = [nd,nd1,nd2]
    return result

# converts data from a abstraction layer into data
def outputData():
    nd = Node()
    nd.data = 1
    nd1 = Node()
    nd1.data = 1
    nd2 = Node()
    nd2.data = 1
    result = [nd,nd1,nd2]
    return result

inputs = inputData()
outputs = outputData()

testNet = Network().generate(inputs,outputs,4,20,False,True)
testNet.draw(512,512)

testNet.print(True)
