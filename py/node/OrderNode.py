from node.Node import Node

class OrderNode(Node):

    def __init__(self, data):
        Node.__init__(self, data)
        Node.type = 0

    def __str__(self):
        return '^'

    def compute(acc, data):
        return acc ^ data
