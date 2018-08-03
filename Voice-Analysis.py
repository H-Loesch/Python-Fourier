#This is the file for actually doing fourier analysis maybe.
#not sure if these category markers will actually be useful, but I guess we'll see. 

#scipy import #scientific tools (fourier analysis, for example)
import numpy #math things
import matplotlib.pylab as plt #plotting module


#Methods

#plots a single x-y figure.
#Also allows labelling of x and y axis, and an input string (all in that order)
def onePlot(xAxis, yAxis, inputString="b-", labelX="X-axis", labelY="Y-axis"):
    plt.plot(xAxis, yAxis, inputString)
    graphNow(labelX, labelY)

#Define x- and y- labels, and display the graph. 
def graphNow(labelX="X-axis", labelY="Y-axis"):
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.show()

#data retrieval 


#data analysis/processing


#data display


#closing


