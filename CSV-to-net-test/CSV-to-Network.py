import sys


if len(sys.argv) <=1:
    quit()
print(sys.argv[1])
drum = {}

drum[35] = drum[36] = 1 #bass drum
drum[41] = drum[43] = drum[45] = drum[47] = drum[48] = drum[50] = drum[61] = drum[76] = 2 #toms
drum[33] = drum[37] = drum[38] = drum[40] = drum[54] = drum[56] = drum[70] = drum[83] = drum[82] = drum[81] = 3 #snares
drum[53] = drum[49] = drum[51] = drum[52] = drum[55] = drum[57] = drum[59] = drum[69] = 4 #cymbals
drum[42] = drum[44] = drum[46] = 5 #Hi-Hat

division = 120

def read_instrument(track,fp,line,values):
    instrument = []
    current_time = 0
    current_note = 0
    current_velocity = 0
    cnt = 0
    instrument.append([None,None])

    while int(values[0]) < track:
        line = fp.readline()
        values = line.split(', ')
        values[-1] = values[-1].strip()

    while int(values[0]) == track:
        if current_time == int(values[1]) and (((values[2] == "Note_on_c") and instrument[cnt][1] != None) or ((values[2] == "Note_off_c") and instrument[cnt][0] != None)):
            line = fp.readline()
            values = line.split(', ')
            values[-1] = values[-1].strip()
            continue
        if current_time < int(values[1]):
            if(instrument[cnt][0] == None):
                instrument[cnt][0] = (0,0,0)
            if(instrument[cnt][1] == None):
                instrument[cnt][1] = (0,0,0)
            while current_time < int(values[1]):
                instrument.append([(0,0,0),(0,0,0)])
                current_time = current_time + division
        cnt = len(instrument)-1
        if(values[2] == "Note_on_c"):
            instrument[cnt][1] = (1,int(values[4]),int(values[5]))
        elif(values[2] == "Note_off_c"):
            instrument[cnt][0] = (-1,int(values[4]),int(values[5]))

        line = fp.readline()
        values = line.split(', ')
        values[-1] = values[-1].strip()
    if(instrument[cnt][0] == None):
        instrument[cnt][0] = (0,0,0)
    if(instrument[cnt][1] == None):
        instrument[cnt][1] = (0,0,0)
    return (instrument,line,values)

def fix_instrument(instrument):
    new_vals = []
    on = 0
    note = 0
    velocity = 0
    for i in range(len(instrument)):
        if on == 0:
            if instrument[i][1][0]==1:
                note = instrument[i][1][1]
                velocity = instrument[i][1][2]
                new_vals.append((1, note, velocity))
                on = 1
            else:
                new_vals.append((0,0,0))
        else:
            new_vals.append((2, note, velocity))
            if instrument[i][0][0]== -1:
                note = 0
                velocity = 0
                on = 0
    return new_vals


def read_drums(track,fp,line,values):
    instrument = []
    current_time = 0
    current_velocity = 0
    instrument.append([0,0,0,0,0])

    while int(values[0]) < track:
        line = fp.readline()
        values = line.split(', ')
        values[-1] = values[-1].strip()

    while int(values[0]) == track:
        if current_time < int(values[1]):
            while current_time < int(values[1]):
                instrument.append([0,0,0,0,0])
                current_time = current_time + division
        if(values[2] == "Note_on_c"):
            if int(values[4]) in drum:
                instrument[-1][int(drum[int(values[4])])-1] = 1
            else:
                instrument[-1][0] = 3
                print("WRONG " + values[4])
        line = fp.readline()
        values = line.split(', ')
        values[-1] = values[-1].strip()
    return instrument, line, values


fp = open(sys.argv[1], 'r')

drums = []
bass = []
guitar = []

line = fp.readline()
values = line.split(", ")
values[-1] = values[-1].strip()

if(values[5] != "960"):
    print("NOT 960")
    exit()

#DRUMS
drums,line,values = read_drums(2,fp,line,values)
#BASS
bass,line,values = read_instrument(3,fp,line,values)
bass = fix_instrument(bass)
#GUITAR
#guitar,line,values = read_instrument(4,fp,line,values)

lent = max(len(drums), len(bass))

for i in range(lent - len(drums)):
    drums.append([0,0,0,0,0])
for i in range(lent - len(bass)):
    bass.append((0,0,0))
fp.close()


import os

name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
#os.remove(name + ".txt")
fp = open("../Network-Input/" + name + ".txt", 'w')

cnt = 0

lead = bass

#Only beats
for i in range(len(drums)):
    fp.write(str(lead[i][0]) + " "  + str(lead[i][1]) + " " + ' '.join(map(str,drums[i])) + "\n")

#all Values
#for i in range(len(drums)):
#    fp.write(' '.join(map(str,guitar[i][0])) + " " + ' '.join(map(str,guitar[i][1])) + " ")
#    fp.write(' '.join(map(str,bass[i][0])) + " " + ' '.join(map(str,bass[i][1])) + " ")
#    fp.write(' '.join(map(str,drums[i][0])) + " " + ' '.join(map(str,drums[i][1])) + "\n")
#    cnt =cnt+division

fp.close()
