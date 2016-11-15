from node.Node import Node

class SubtractorNode(Node):

    def __init__(self, data):
        Node.__init__(self, data)

    def __str__(self):
        return '-'

    def compute(acc, data):
        return acc - data