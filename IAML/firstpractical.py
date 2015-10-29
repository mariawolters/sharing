#!/bin/python

import numpy
import matplotlib.pyplot as plt


emails = 200
pHam = 0.7
timeSpamSec = 5

nHams = numpy.random.binomial(emails,pHam,1)

spam = emails - nHams

timeSpamTotalMin = (spam * timeSpamSec) / 60

nHams = numpy.random.binomial(200,0.7,250)

nSpams = emails - nHams

plt.plot(nSpams)

plt.show()

freqs, bins = numpy.histogram(nSpams,bins=max(nSpams)-min(nSpams))

plt.bar(bins[:-1],freqs,width=1)

plt.ylim(0,max(freqs)+5)

plt.xlim(min(nSpams)-5,max(nSpams+5))

plt.show()


timeSpamTotalMin = (nSpams * timeSpamSec) / 60

numpy.mean(timeSpamTotalMin)

numpy.std(timeSpamTotalMin)

sum(timeSpamTotalMin) 
