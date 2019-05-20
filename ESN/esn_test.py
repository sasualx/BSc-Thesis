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

rc('text', usetex=True)
rc('font', family='serif')

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

figure(11).clear()
f11 = figure(11)
xlabel(r'\textbf{Time}', fontsize=11)
ylabel(r'\textbf{Value}', fontsize=11)
plot( data[500:550,0], 'k' )
plot( target[500:550,0], 'b', alpha=0.7 )
plot( target[500:550,1], 'm', alpha=0.7 )
plot( target[500:550,2], 'r', alpha=0.7 )
plot( target[500:550,3], 'y', alpha=0.7 )
plot( target[500:550,4], 'g', alpha=0.7 )
title(r'\textbf{Input training Data}', fontsize=11)
legend([r'\normalfont{Bass Line Notes Played}', r'\normalfont{Target Bass Drum Data}', r'\normalfont{Target Tom Data}',r'\normalfont{Target Snare Data}', r'\normalfont{Target Cymbal Data}', r'\normalfont{Target Hi-Hat Data}'], fontsize=11)


figure(0).clear()
f0 = figure(0)
plot( target[500:600,0], 'k' )
title(r'\textbf{Bass Drum}', fontsize=11)

figure(1).clear()
f1 = figure(1)
plot( target[500:600,1], 'k' )
title(r'\textbf{Tom Drum}', fontsize=11)


figure(2).clear()
f2 = figure(2)
plot( target[500:600,2], 'k' )
title(r'\textbf{Snare Drum}', fontsize=11)

figure(3).clear()
f3 = figure(3)
plot( target[500:600,3], 'k' )
title(r'\textbf{Cymbal}', fontsize=11)

figure(4).clear()
f4 = figure(4)
plot( target[500:600,4], 'k' )
title(r'\textbf{Hi-Hat}', fontsize=11)




figure(5).clear()
f5 = figure(5)
plot(target[500:600,0],'b')
plot( Y[500:600,0], 'k' )
xlabel(r'\textbf{Time}', fontsize=11)
ylabel(r'\textbf{Value}', fontsize=11)
title(r'\textbf{Bass Drum}', fontsize=11)
legend([r'\textbf{Target Bass Drum}',r'\textbf{Generated Bass Drum}'], fontsize=11)

figure(6).clear()
f6 = figure(6)
plot(target[500:1000,1],'b')
plot( Y[500:1000,1], 'k' )
title(r'\textbf{Generated Tom Drum}', fontsize=11)


figure(7).clear()
f7 = figure(7)
plot(target[500:600,2],'b')
plot( Y[500:600,2], 'k' )
xlabel(r'\textbf{Time}', fontsize=11)
ylabel(r'\textbf{Value}', fontsize=11)
title(r'\textbf{Snare Drum}', fontsize=11)
legend([r'\textbf{Target Snare Drum}',r'\textbf{Generated Snare Drum}'], fontsize=11)


figure(8).clear()
f8 = figure(8)
plot(target[500:600,3],'b')
plot( Y[500:600,3], 'k' )
xlabel(r'\textbf{Time}', fontsize=11)
ylabel(r'\textbf{Value}', fontsize=11)
title(r'\textbf{Cymbal}', fontsize=11)
legend([r'\textbf{Target Cymbal}',r'\textbf{Generated Cymbal}'], fontsize=11)


figure(9).clear()
f9 = figure(9)
plot(target[500:600,4],'b')
plot( Y[500:600,4], 'k' )
title(r'\textbf{Hi-Hat}', fontsize=11)
xlabel(r'\textbf{Time}', fontsize=11)
ylabel(r'\textbf{Value}', fontsize=11)
legend([r'\textbf{Target Hi-Hat}',r'\textbf{Generated Hi-Hat}'], fontsize=11)

f7.savefig("Generated_Snare.pdf", bbox_inches='tight')
f8.savefig("Generated_Cymbal.pdf", bbox_inches='tight')
f5.savefig("Generated_Bass_Drum.pdf", bbox_inches='tight')
f11.savefig("Input_Data.pdf", bbox_inches='tight')
f9.savefig("Generated_High_Hat.pdf", bbox_inches='tight')
'''
f0.savefig("Bass_Drum.pdf", bbox_inches='tight')
f1.savefig("Tom.pdf", bbox_inches='tight')
f2.savefig("Snare.pdf", bbox_inches='tight')
f3.savefig("Cymbal.pdf", bbox_inches='tight')
f4.savefig("High_Hat.pdf", bbox_inches='tight')
f5.savefig("Generated_Bass_Drum.pdf", bbox_inches='tight')
f6.savefig("Generated_Tom.pdf", bbox_inches='tight')
f7.savefig("Generated_Snare.pdf", bbox_inches='tight')
f8.savefig("Generated_Cymbal.pdf", bbox_inches='tight')
f9.savefig("Generated_High_Hat.pdf", bbox_inches='tight')
'''
