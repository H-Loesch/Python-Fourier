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
    #Huh. So that's how python methods are commented, I guess. Neat?

    [sampleRate, aud_data] = wav.read(fileName)
    assert (len(aud_data) != 0), "Audio file is empty."

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
    xAxis = xAxis[0:sampleNum-(sampleNum % size)] #ensures that this is divisible by size
    
    fourier = abs(fourierArray)[0:(sampleNum - (sampleNum % size))] #make sure this is divisible by size. We're cutting off most so it's fine.
    fourier = numpy.split(fourier, size)[0]
    xAxis = numpy.split(xAxis, size)[0]
    plt.semilogx(xAxis, fourier)

    peaks = []
    max = 0
    maxLocation = 0
    peaks = [0] #make into array later
    peakLocations = [0] #make into array later
    HZ = size*len(xAxis)/sampleRate #a constant that converts between elements of the arrays and Hz

    #this for loop iterates through our arrays at about .25Hz / cycle. Which is a slightly low resolution, but this is a rough check, so that's fine.
    #also, I'm doing this manually instead of using a function so that I can skip the area around previous peaks.
    for a in range(3): #only doing two for this test. I'll learn how to do array comparisons in the morning.
        i = 0 
        place = 0 #In c++ it's best to allocate variables before loops. I have no idea if this applies in Python.
        while i < len(xAxis) - 10: #fix this later
            i = i + size*len(xAxis)/(sampleRate*4)
            place = int(round(i))

            if (place > peakLocations[a] - 30*HZ) & (place < peakLocations[a] + 30*HZ):
               # print("skipped spot is: ", xAxis[place])
                i = peakLocations[a] + 30*HZ #skip the already-peaked region. This is why we're using a while loop (I don't trust python for loops yet)
                xAxis[int(round(i))]
            if (place > peakLocations[a-1] - 30*HZ) & (place < peakLocations[a-1] + 30*HZ):
                #print("skipped spot is: ", xAxis[place])
                i = peakLocations[a] + 30*HZ #skip the already-peaked region. This is why we're using a while loop (I don't trust python for loops yet)
                xAxis[int(round(i))]
            if (fourier[place] > max):
                 max = fourier[place] #Needs to be an integer to be an index
                 maxLocation = place
                # print("New goodplace is:", place)
        peaks.append(max)
        peakLocations.append(maxLocation)
        max = 0
        #print(maxLocation)
        maxLocation = 0
    #end
    print("Fourier spectrum peaks are: ", peakLocations[1]/HZ, peakLocations[2]/HZ, peakLocations[3]/HZ)
    
    #I know the above is nasty. And it's got testing code still in there. But whatever.

#int main() {
#//////////////////////////////////////////////////////////////////////////////
'''
plt.subplot(2, 1, 1)
plotFourierFile("ASample1Clean.wav")
plt.title("A's Sample 1") 


plt.subplot(2, 1, 2)
plt.title("A's Sample 2") 
#plt.xlabel("Frequency (Hz)")
plotFourierFile("Asample2Clean.wav")

plt.subplot(2, 1, 2)
plt.title("My sample 1")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude") 
plotFourierFile("MSample1Clean.wav")
'''
plt.subplot(111)
plt.title("My sample 2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude") 
plotFourierFile("MSample2Clean.wav")

plt.show()


'''current ideas for comparison/identification method:
find the peak of the fourier array
store its frequency somewhere
find the peak again, excluding the zone, like... 40Hz to either side of the old one. (or some amount like that)
repeat until we have 3-4 peaks
Then we can use the location of those peaks as a VERY crude identification of the speaker

Please keep in mind I'm working on limited time, knowledge, and also this is my first draft of the idea, so. 
I don't really have the time, resources, or audio equipment to really create a sophisticated or even good system for this.

Range around each peak should be expanded based on the peak's frequency

Testing the system as it is now (aka bad), it works for A's samples, but not for mine.
To be fair, mine are weird due to me only having a cheap headset to record one, but that's... how it is sometimes. 
Anyway. Maybe require at least one peak be in the 100-300 range? Since that's where basically all people's first harmonic is. Or was it 0th?
Yeah, it doesn't work for either of my samples. I know that my speaking style is a little weird and pitch-variant, so that may be part of the problem.
Requiring one peak to be in the 100-300 range is probably a good idea.
That, or the idea re: the inaccessible range around each peak being expanded as the frequency increases. 

Maybe take the average of a small range of elements? I know a way to walk through and gather averages that's only a little less efficient than doing 'em singularly
Might help with weird outlier elements.

From here, comparison between voice samples isn't too far off
    Maybe, like. Just something about taking the average of the three peaks for each sample, and if they're >20 different then reject?
    That's... probably a bad idea. 
    Maybe compare the most similar peaks between both samples. And if >1 of them is significantly different then reject
        So if the furthest apart peaks are 150Hz and 170Hz, then that's fine
        But if there's that, AND 240Hz and 200Hz, then reject.
'''
