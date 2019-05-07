from numpy import *
from matplotlib.pyplot import *
import scipy.linalg
from Parameters import *
import pdb
Win = loadtxt("Win.txt")
W = loadtxt("W.txt")
Wout = loadtxt("Wout.txt")


load = loadtxt('test.txt')
data = load[:,0:inSize]
target = load[:,inSize:inSize+outSize]

testLen = data.shape[0]

# run the trained ESN in a generative mode. no need to initialize here,
# because x is initialized with training data and we continue from there.
Y = zeros((outSize,testLen))
x = zeros((resSize,1))
u = data[0].reshape(inSize,1)
fp = open("output.txt","w")
for t in range(testLen-1):
    x = (1-a)*x + a*tanh( dot( Win, vstack((1,u)) ) + dot( W, x ) )
    y = dot( Wout, vstack((1,u,x)) )
    Y[:,t] = y.reshape(outSize) * 4
    u = data[t+1].reshape(inSize,1)

Y = Y.T
print(Y.shape)
fp = open("output.txt","w")
for line in Y:
    fp.write(' '.join(map(str,line))+"\n")
    #if line[0]>0.5:
    #    fp.write(str(1)+"\n")
    #else:
    #    fp.write(str(0)+"\n")
fp.close()
#pdb.set_trace()

figure(2).clear()
plot( data[300:400,0], 'g' )
plot( target[300:400], 'b' )
title('Data and target data starting at $n=300$')
legend(['Input Data', 'Target Data'])

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
