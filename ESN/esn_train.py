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
import time
from Parameters import *


# load the data
#pdb.set_trace()
start = time.time()
load = loadtxt('train.txt')
data = load[:,0:inSize]
target = load[:,inSize:inSize+outSize]
end = time.time()
print("Loaded Data in " + str(end - start) + " seconds.")

trainLen = data.shape[0]
initLen = 5000


# generate the ESN reservoir

random.seed(42)
start = time.time()
Win = (random.rand(resSize,1+inSize)-0.5) * input_scaling
W = zeros((resSize,resSize))
for idx in range(resSize):
    connections = arange(resSize)
    random.shuffle(connections)
    connections = connections[:fixed_node_connection]
    for con in connections:
        W[idx][con] = random.rand() - 0.5

spectral_radius = max(abs(linalg.eig(W)[0]))
while spectral_radius > 1:
    W /= spectral_radius
    spectral_radius = max(abs(linalg.eig(W)[0]))
end = time.time()
print("Generated Reservoir in " + str(end - start) + " seconds.")
#W *= 1.25 / rhoW

# allocated memory for the design (collected states) matrix
X = zeros((1+inSize+resSize,trainLen-initLen))
# set the corresponding target matrix directly
Yt = target[initLen:trainLen].T
start = time.time()
# run the reservoir with the data and collect X
x = zeros((resSize,1))
for t in range(trainLen):
    u = data[t].reshape(inSize,1)
    x = (1-a)*x + a*tanh( dot( Win, vstack((1,u)) ) + dot( W, x ) )
    if t >= initLen:
        X[:,t-initLen] = vstack((1,u,x))[:,0]
end = time.time()
print("Generated X in " + str(end - start) + " seconds.")

start = time.time()
# train the output by ridge regression
reg = 1e-8  # regularization coefficient
X_T = X.T
Wout = dot( dot(Yt,X_T), linalg.inv( dot(X,X_T) + \
    reg*eye(1+inSize+resSize) ) )
end = time.time()

print("Computed Wout in " + str(end - start) + " seconds.")

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
    fp.write(' '.join(map(str,line))+"\n")
fp.close()
