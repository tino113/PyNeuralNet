from network import Network
from node import Node


# determines the fitness of a network
def fitness():
    pass

# converts data from a source into nodes for first abstraction layer
def inputData():
    nd = Node()
    nd.data = 1
    result = [nd]
    return result

# converts data from a abstraction layer into data
def outputData():
    pass

inputs = inputData()
outputs = []

testNet = Network().generate(inputs,outputs,1,4,False,True)

testNet.print(True)
