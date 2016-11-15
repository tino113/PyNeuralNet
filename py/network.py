from py.abstractionLayer import AbstractionLayer
from random import randint
import tkinter as tk
from threading import Thread
from py.mathFuncs import hsvTohex
from py.axiom import Axiom
from py.mathFuncs import sigmoid
from random import uniform

class Network:

    def __init__(self):
        self.abstractionLayers = []
        self.inputNodes = []
        self.outputNodes = []
        self.axiomOutList = []

    def print(self, verbose = False):
        print("Network: " + str(self))
        if verbose:
            for aL in self.abstractionLayers:
                aL.print(True)

    def drawThreaded(self,w=256,h=256):
        root = tk.Tk()
        canvas = tk.Canvas(root,
                           width=w,
                           height=h,
                           borderwidth=0,
                           highlightthickness=0,
                           bg="black")
        canvas.grid()

        r = 15
        rowCollMin = h

        nodeDict = {}

        Cols = w/(len(self.abstractionLayers) + 3)
        i = 0
        Rows = h/(len(self.inputNodes)+1)
        if Cols < rowCollMin:
            rowCollMin = Cols
        if Rows < rowCollMin:
            rowCollMin = Rows
        for inputNode in self.inputNodes:
            # space regularly in y
            x, y = Cols,Rows*(i+1)
            nodeDict.update({inputNode : (x,y,"blue")})
            i+=1

        i = 0
        for layer in self.abstractionLayers:
            # space regularly in x
            x = Cols*(i+2)
            j = 0
            Rows = h/(len(self.abstractionLayers[i].nodes)+1)
            if Rows < rowCollMin:
                rowCollMin = Rows
            for node in self.abstractionLayers[i].nodes:
                y = Rows*(j+1)
                nodeDict.update({node : (x,y,"red")})
                j+=1
            i+=1

        i = 0
        Rows = h/(len(self.outputNodes)+1)
        if Rows < rowCollMin:
            rowCollMin = Rows
        for outputNode in self.outputNodes:
            # space regularly in y
            x, y = Cols*(len(self.abstractionLayers)+2),Rows*(i+1)
            nodeDict.update({outputNode : (x,y,"green")})
            i+=1

        # draw all axioms in one go
        i = 0
        for layer in self.abstractionLayers:
            for axiom in layer.axiomList:
                #xs,ys,xe,ye = 10,(j+1)*10,w-10,(j+1)*10 # DEBUG: visualize all axioms
                fromCoord = nodeDict[axiom.nodeFrom]
                xs, ys = fromCoord[0],fromCoord[1]
                toCoord = nodeDict[axiom.nodeTo]
                xe, ye = toCoord[0],toCoord[1]
                canvas.create_line(xs,ys,xe,ye,fill=hsvTohex(0,1,axiom.weight/2+0.5))
            i+=1

        for axiom in self.axiomOutList:
            fromCoord = nodeDict[axiom.nodeFrom]
            xs, ys = fromCoord[0],fromCoord[1]
            toCoord = nodeDict[axiom.nodeTo]
            xe, ye = toCoord[0],toCoord[1]
            canvas.create_line(xs,ys,xe,ye,fill=hsvTohex(0,1,axiom.weight/2+0.5))

        r = rowCollMin/4

        # draw all nodes in one go
        for node, values in nodeDict.items():
            x,y,c = values[0],values[1],values[2]
            canvas.create_oval(x-r,y-r,x+r,y+r,fill=c)

        root.wm_title("Network: " + str(self))
        root.mainloop()
        print ("drawing finished...exiting")

    def draw(self,w=256,h=256):
        thread = Thread(target = self.drawThreaded, args = (w,h))
        thread.start()

    # generates a new random network, max layers, max nodes per layer and max
    # axiom weighting can all be determined
    def generate(self,inputNodes,outputNodes,numAbstractions,numNodesPerLayer,abstractionsMax = False, nodesPerLayerMax = False):
        self.inputNodes = inputNodes
        self.outputNodes = outputNodes

        if abstractionsMax:
            numAbstractions = randint(1, numAbstractions)

        for i in range(numAbstractions):
            aL = AbstractionLayer()
            if nodesPerLayerMax:
                numNodesPerLayer = randint(len(self.outputNodes), numNodesPerLayer) # ensures diminishing tree to the right
            if i > 0:
                self.abstractionLayers.append(aL.create(self.abstractionLayers[i-1].nodes))
            else:
                self.abstractionLayers.append(aL.create(self.inputNodes))

            for j in range(numNodesPerLayer):
                aL.addNewNode()

        for outNode in self.outputNodes:
            axOut = []
            for prevN in self.abstractionLayers[-1].nodes:
                ax = Axiom()
                axOut.append(ax.create(prevN,outNode,sigmoid(uniform(-1,1))))
            self.axiomOutList.extend(axOut)

        return self

    def go(self):
        for aL in self.abstractionLayers:
            aL.go()

    # on a new birth there is a small chance of mutation of axiom weights,
    # a smaller chance of creating a new node in an existing abstraction layer,
    # and an even smaller chance of creating an entirely new abstraction layer.
    def mutate(self):
        pass

    # can be asexual or sexual, random weighting is used to determine the amount
    # of genetic data shared between parents, may contain 1 to n partners
    # N.B. Not limited to 1 or 2 partners
    def reproduce(self):
        pass


