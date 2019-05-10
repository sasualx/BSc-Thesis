
import pdb
from numpy import *
from matplotlib.pyplot import *
import scipy.linalg
import time
from Parameters import *

start = time.time()
load = loadtxt('train.txt')
data = load[:,0:inSize]
target = load[:,inSize:inSize+outSize]
end = time.time()
print("Loaded Data in " + str(end - start) + " seconds.")

trainLen = data.shape[0]
initLen = 5000

random.seed(42)
start = time.time()
Win = (random.rand(resSize,1+inSize)-0.5)
Win[:,0] = Win[:,0] * input_scaling[0]
Win[:,1:inSize+1] = Win[:,1:inSize+1] * input_scaling[1]
W = zeros((resSize,resSize))
for idx in range(resSize):
    connections = arange(resSize)
    random.shuffle(connections)
    connections = connections[:fixed_node_connection]
    for con in connections:
        W[idx][con] = random.rand() - 0.5

spectral_radius = max(abs(linalg.eig(W)[0]))
W = W / spectral_radius * desired_spectral_radius
end = time.time()
print("Generated Reservoir in " + str(end - start) + " seconds.")

X = zeros((1+inSize+resSize,trainLen-initLen))
Yt = target[initLen:trainLen].T
start = time.time()

x = zeros((resSize,1))
for t in range(trainLen):
    u = data[t].reshape(inSize,1)
    x = (1-a)*x + a*tanh( dot( Win, vstack((1,u)) ) + dot( W, x ) )
    if t >= initLen:
        X[:,t-initLen] = vstack((1,u,x))[:,0]
end = time.time()
print("Generated X in " + str(end - start) + " seconds.")

start = time.time()
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
