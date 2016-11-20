import tkinter as tk
from threading import Thread
from mathFuncs import hsvTohex

class Visualization:

    def __init__(self, inputs, outputs, abstraLayers, axiomsOut):
        self.abstractionLayers = abstraLayers
        self.inputNodes = inputs
        self.outputNodes = outputs
        self.axiomOutList = axiomsOut

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
