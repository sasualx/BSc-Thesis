from numpy import *

drum = {}
drum[0] = '36' #bass drum
drum[1] = '41' #toms
drum[2] = '38' #snares
drum[3] = '49' #cymbals
drum[4] = '42' #Hi-Hat

threshhold = [0.4,0.05,0.25,0.11,0.4]

with open('output.txt') as f:
    content = f.readlines()

delimiter = 120
time = 0
random.seed(42)
wr = open('result.txt','w')

for line in content:
    i = line.split()
    for idx in range(len(i)):
        ok = False
        if(float(i[idx]) >= threshhold[idx]):
            wr.write("2, " + str(time) + ", Note_on_c, 9, " + drum[idx] + ", 95\n")
            ok = True
    if ok:
        wr.write("2, " + str(time+delimiter) + ", Note_off_c, 9, 0, 0\n")
    time = time + delimiter
wr.write("2, " + str(time) + ", End_track\n")


wr.close()
