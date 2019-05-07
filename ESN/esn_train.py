"""
A minimalistic Echo State Networks demo with Mackey-Glass (delay 17) data
in "plain" scientific Python.
by Mantas LukoÅ¡eviÄius 2012-2018
http://mantas.info
"""
import pdb
from numpy import *
from matplotlib.pyplot import *
import scipy.linalg

from Parameters import *


# load the data
#pdb.set_trace()
load = loadtxt('train.txt')
data = load[:,0:inSize]
target = load[:,inSize:inSize+outSize]
print("Loaded Data")

trainLen = data.shape[0]
initLen = 5000


# generate the ESN reservoir

random.seed(42)
Win = (random.rand(resSize,1+inSize)-0.5) * 1
fixed_node_connection = 10
W = None
for idx in range(resSize):
    connections = arange(resSize)
    random.shuffle(connections)
    connections = connections[:fixed_node_connection]
    newRow = zeros(resSize)
    for con in connections:
        newRow[con] = random.rand() - 0.5
    if W is None:
        W = [newRow]
    else:
        W = append(W, [newRow], axis = 0)

spectral_radius = max(abs(linalg.eig(W)[0]))
while spectral_radius > 1:
    W /= spectral_radius
    spectral_radius = max(abs(linalg.eig(W)[0]))

print("Generated Reservoir")
#W *= 1.25 / rhoW

# allocated memory for the design (collected states) matrix
X = zeros((1+inSize+resSize,trainLen-initLen))
# set the corresponding target matrix directly
Yt = target[initLen:trainLen].T

# run the reservoir with the data and collect X
x = zeros((resSize,1))
for t in range(trainLen):
    u = data[t].reshape(inSize,1)
    x = (1-a)*x + a*tanh( dot( Win, vstack((1,u)) ) + dot( W, x ) )
    if t >= initLen:
        X[:,t-initLen] = vstack((1,u,x))[:,0]

print("Generated X")

# train the output by ridge regression
reg = 1e-8  # regularization coefficient
X_T = X.T
Wout = dot( dot(Yt,X_T), linalg.inv( dot(X,X_T) + \
    reg*eye(1+inSize+resSize) ) )

print("Computed Wout")

fp = open("Win.txt","w")
for line in Win:
    fp.write(' '.join(map(str,line))+"\n")
fp.close()
fp = open("W.txt","w")
for line in W:
    fp.write(' '.join(map(str,line))+"\n")
fp.close()
fp = open("Wout.txt","w")
for line in Wout:
    print(' '.join(map(str,line)))
    fp.write(' '.join(map(str,line))+"\n")
fp.close()
