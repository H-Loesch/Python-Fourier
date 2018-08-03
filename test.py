#scipy import #scientific tools (fourier analysis, for example)
import numpy #math things
import matplotlib.pylab as plt #plotting module

print("oh hey. Good to see you here.")
xAxis = numpy.linspace(1, 7)

yAxisPi = []
yAxisNum = []
for xVal in xAxis:
    yAxisPi.append(numpy.sin(xVal*2*numpy.pi))
    yAxisNum.append(numpy.sin(xVal))

plt.plot(xAxis, yAxisNum, 'b-')
plt.plot(xAxis, yAxisPi, 'r-')
plt.show()

#plt.plot(xAxis, yAxisNum)
#plt.show
