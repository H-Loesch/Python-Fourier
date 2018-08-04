#This is the file for actually doing fourier analysis maybe.
#not sure if these category markers will actually be useful, but I guess we'll see. 

#scipy import #scientific tools (fourier analysis, for example)
from numpy import fft
import numpy
import matplotlib.pylab as plt #plotting module
from scipy.io import wavfile as wav #allows working with *.wav files in a numpy format.

#Methods
#//////////////////////////////////////////////////////////

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

def plotFourierFile(fileName = ""):
    ''' Plot the fourier transform of audio from a file.'''
    #Huh. So that's how python methods are commented, I guess. Neat, I guess. 

    [sampleRate, aud_data] = wav.read(fileName)
    assert (len(aud_data) != 0), "Audio file was not found."
    
    fourierOut = fft.fft(aud_data)
    plotFourier(sampleRate, fourierOut)

def plotFourier(sampleRate = 32000, fourierArray = []):
    '''Plot a fourier transform.
       Does not show the plot automatically.'''
    sampleNum = len(fourierArray)
    #sampleTimes = numpy.linspace(0, sampleNum / sampleRate, sampleNum) #array of sample timestamps. Not used, but may be useful?
    sampleLength = sampleNum / sampleRate #duration of audio signal (seconds)
    xAxis = numpy.arange(0, sampleNum, 1/sampleLength)
    xAxis = xAxis[0:sampleNum]

    fourier = abs(fourierArray)
    fourier = numpy.split(fourier, 2)[0] #divides into the first half, since the second is a mirror of the first.
    xAxis = numpy.split(xAxis, 2)[0]

    plt.plot(xAxis, fourier)

#data retrieval 
#//////////////////////////////////////////////////////////

#reads from the given file, and returns an array of the sample rate, and an array of the data
[sampleRate, aud_data] = wav.read("sinewave.wav") #these files should be at 32000Hz, 16-bit signed *.wav
#print(sinewave[1])

#data analysis/processing
#//////////////////////////////////////////////////////////

sampleNum = len(aud_data)
sampleTimes = numpy.linspace(0, sampleNum / sampleRate, sampleNum) #creates array of sample timestamps
sampleLength = sampleNum / sampleRate #Duration of audio signal (seconds)
fourierTransform = abs(fft.fft(aud_data))


#data display
#//////////////////////////////////////////////////////////
xAxis = numpy.arange(0, sampleNum, 1/sampleLength) #Dividing the unit step length by 1/sampleLength ensures the x-axis is scaled correctly
xAxis = xAxis[0:sampleNum]
xAxis = numpy.split(xAxis, 4)[0]
fourierTransform = numpy.split(fourierTransform, 4)[0]
plt.plot(xAxis, fourierTransform, 'b--') 
#plt.plot(numpy.linspace(0, sampleNum, sampleNum), fft.fft(sampleNum * 5* numpy.sin(440 * numpy.pi * 2 * numpy.linspace(0, sampleNum, sampleNum))), 'r-')
#plt.xticks(numpy.arange(0, sampleRate/4, 1000), numpy.arange(0, sampleRate/4, 1000))
plt.title("Comparison of Python-generated waveform with Audacity-waveform for 880 Hz sinewave")
plt.show()
#closing
#//////////////////////////////////////////////////////////