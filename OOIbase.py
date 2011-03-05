import numpy
def import_spectrum(filename):
    """ read notes from .scope file
    example:
    wavelength, counts, params = OOIbase.import_spectrum('glass.Master.scope')
    """
    fd = open(filename,'r')
    params = {}
    wavelength=[]
    counts=[]
    
    params['version info'] = fd.readline()
    
    while 1:
        line = fd.readline()
        if not line:
            print 'hit end of params'
            break
        elif '>>>>>Begin Spectral Data<<<<<' in line:
            break
        elif line:
            sline = line.split(':',1)
            if len(sline)>1:
                params[sline[0]] = sline[1]
    
    while 1:
        line = fd.readline()
        if not line:  # 'readline()' returns None at end of file.
            break
        elif '>>>>>End Spectral Data<<<<<' in line:
            break
        elif line:
            sline = line.split()
            wavelength.append(float(sline[0]))
            counts.append(float(sline[1]))
    
    wavelength = numpy.array(wavelength)
    counts = numpy.array(counts)
    return 	wavelength, counts, params
