import OOIbase
import numpy as np
import os, pylab
pylab.ion()

dirName = './indoorRotator/day2'
#dirName = './day6'
fileNames = os.listdir(dirName)

fig = pylab.figure()
ax = fig.add_subplot(111)

for fileName in fileNames:
    if fileName[-5:] == 'scope':
        wavelength, counts, params = OOIbase.import_spectrum(os.path.join(dirName,fileName))
        cmin = np.mean(counts[wavelength<300])
        #l = ax.plot(wavelength,(counts-cmin)/(sum(counts-cmin)))
        l = ax.plot(wavelength,counts-cmin)
        l[0].set_label(fileName+params['Integration Time (msec)'][:3])

ax.legend(loc='upper left')
pylab.draw()
