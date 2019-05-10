#!/usr/bin/env python

from numpy import *
from matplotlib.pyplot import *
import scipy.linalg
from Parameters import *
import pdb
import math
Win = loadtxt("Win.txt")
W = loadtxt("W.txt")
Wout = loadtxt("Wout.txt")


def prob_fct(p,y):
    r = 0
    if y == 1 :
        r = p
    else:
        r = 1 - p
    if r <= 0.000001:
        r = 0.000001
    return r

def compute_error_metric(Y,target):
    res = 0
    for l1,l2 in zip(Y,target):
        for p,y in zip(l1,l2):
            res = res + math.log(prob_fct(p,y))
    return res

load = loadtxt('test.txt')
data = load[:,0:inSize]
target = load[:,inSize:inSize+outSize]
testLen = data.shape[0]

Y = zeros((outSize,testLen))
x = zeros((resSize,1))
u = data[0].reshape(inSize,1)
fp = open("output.txt","w")
for t in range(testLen-1):
    x = (1-a)*x + a*tanh( dot( Win, vstack((1,u)) ) + dot( W, x ) )
    y = dot( Wout, vstack((1,u,x)) )
    Y[:,t] = y.reshape(outSize) * 2
    u = data[t+1].reshape(inSize,1)

Y = Y.T
print(compute_error_metric(Y,target))
fp = open("output.txt","w")
for line in Y:
    fp.write(' '.join(map(str,line))+"\n")
fp.close()

figure(2).clear()
plot( data[300:400,0], 'g' )
plot( target[300:400], 'b' )
title('Data and target data starting at $n=300$')
legend(['Input Data', 'Target Data'])

figure(4).clear()
plot( Y[300:400,0], 'g' )
plot( Y[300:400,1], 'b' )
plot( Y[300:400,2], 'r' )
plot( Y[300:400,3], 'y' )
plot( Y[300:400,4], 'k' )
title('Generated Data $n=300$')
legend(['BASS DRUM', 'TOM', 'SNARE', 'CYMBAL', 'HI-HAT'])

figure(5).clear()
plot( Y[200:1000,0], 'g' )
title('Data and target data starting at $n=300$')
legend(['BASS DRUM'])

figure(6).clear()
plot( Y[200:1000,1], 'b' )
title('Data and target data starting at $n=300$')
legend(['TOM'])


figure(7).clear()
plot( Y[200:1000,2], 'r' )
title('Data and target data starting at $n=300$')
legend(['SNARE'])

figure(8).clear()
plot( Y[200:1000,3], 'y' )
title('Data and target data starting at $n=300$')
legend(['CYMBAL'])

figure(9).clear()
plot( Y[200:1000,4], 'k' )
title('Data and target data starting at $n=300$')
legend(['HI-HAT'])

figure(3).clear()
plot( data[300:400,0], 'g' )
plot( Y[300:400], 'b' )
title('Data and generated data starting at $n=300$')
legend(['Input Data', 'generated Data'])

figure(1).clear()
plot( target[300:400], 'r' )
plot( Y[300:400], 'b' )
title('Target and generated signals starting at $n=300$')
legend(['Target signal', 'Generated Signal'])


show()
