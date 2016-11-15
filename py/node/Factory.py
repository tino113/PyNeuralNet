from random import randint
from node.OrderNode import OrderNode
from node.DivisorNode import DivisorNode
from node.MultiplierNode import MultiplierNode
from node.SummationNode import SummationNode
from node.SubtractorNode import SubtractorNode

class Factory:

    @staticmethod
    def create(data = 0):
        seed = randint(0, 4)
        if (seed == ORDER):
            return OrderNode(data)
        elif (seed == DIVIDE):
            return DivisorNode(data)
        elif (seed == MULTIPLY):
            return MultiplierNode(data)
        elif (seed == SUM):
            return SummationNode(data)
        elif (seed == SUBTRACT):
            return SubtractorNode(data)

ORDER = 0

DIVIDE = 1

MULTIPLY = 2

SUM = 3

SUBTRACT = 4
