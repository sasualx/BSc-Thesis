from numpy import *

with open('output.txt') as f:
    content = f.readlines()

delimiter = 40
time = 0

wr = open('result.txt','w')

for line in content:
    i = line.split()
    if(float(i[0]) >= 0.25):
        wr.write("2, " + str(time) + ", Note_on_c, 9, 36, 95\n")
        wr.write("2, " + str(time+delimiter) + ", Note_off_c, 9, 0, 0\n")
    time = time + delimiter
wr.write("2, " + str(time) + ", End_track\n")


# All Drums
'''
for line in content:
    i = line.split()
    if(float(i[0]) >= 0.25):
        wr.write("2, " + str(time) + ", Note_on_c, 9," + str(int(float(i[1]))) + ", 95\n")
        wr.write("2, " + str(time+delimiter) + ", Note_off_c, 9, 0, 0\n")
    time = time + delimiter
wr.write("2, " + str(time) + ", End_track\n")
'''
wr.close()
