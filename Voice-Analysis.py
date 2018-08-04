#This is the file for actually doing fourier analysis maybe.
#not sure if these category markers will actually be useful, but I guess we'll see. 

#scipy import #scientific tools (fourier analysis, for example)
from numpy import fft
import numpy
import matplotlib.pylab as plt #plotting module
from scipy.io import wavfile as wav #allows working with *.wav files in a numpy format.

#Methods
#//////////////////////////////////////////////////////////


def onePlot(xAxis, yAxis, inputString="b-", labelX="X-axis", labelY="Y-axis"):
    '''plots a single x-y figure.
       Also allows labelling of x and y axis, and an input string (all in that order)'''
    plt.plot(xAxis, yAxis, inputString)
    graphNow(labelX, labelY)

#
def graphNow(labelX="X-axis", labelY="Y-axis"):
    "Define x- and y- labels, and display the graph."
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.show()

def plotFourierFile(fileName = "", size = 2):
    ''' Plot the fourier transform of audio from a file.
        size is the fraction of the fourier transform to show.
            Default is 2, since the second half of the transform is a mirror of the first'''
    #Huh. So that's how python methods are commented, I guess. Neat, I guess. 

    [sampleRate, aud_data] = wav.read(fileName)
    assert (len(aud_data) != 0), "Audio file was not found."
    
    fourierOut = fft.fft(aud_data)
    plotFourier(sampleRate, fourierOut, size)

def plotFourier(sampleRate = 32000, fourierArray = [], size = 2):
    '''Plot a fourier transform.
       Does not show the plot automatically.
       Size is the fraction of the fourier transform to show.
        Default is 2, since the second half of the transform is a mirror of the first'''
    sampleNum = len(fourierArray)
    #sampleTimes = numpy.linspace(0, sampleNum / sampleRate, sampleNum) #array of sample timestamps. Not used, but may be useful?
    sampleLength = sampleNum / sampleRate #duration of audio signal (seconds)
    xAxis = numpy.arange(0, sampleNum, 1/sampleLength)
    xAxis = xAxis[0:sampleNum]

    fourier = abs(fourierArray)
    fourier = numpy.split(fourier, size)[0] 
    xAxis = numpy.split(xAxis, size)[0]
    print(sampleRate)
    plt.semilogx(xAxis[75:len(xAxis)], fourier[75:len(xAxis)]) #cutting off first 75, so that the rest of the waveform is actually shown
    #the first 75 tend to not matter very much, anyway.
#int main() {
#//////////////////////////////////////////////////////////////////////////////

plotFourierFile("voice1.wav", 2)
plt.title("Comparison of idle vocal, Audacity v Program")
plt.show()
#graphNow("Frequency (HZ)", "Magnitude")