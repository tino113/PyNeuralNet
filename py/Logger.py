
class Logger:

    def __init__(self, verbose = False):
        self.verbose = verbose

    def outputNode(self, node):
        print("Node: " + str(node) + " data: " + str(node.data))

        if self.verbose:
            print("Node: " + str(node) + " axioms:")
            for axiom in node.axiomsIn:
                axiom.print()
