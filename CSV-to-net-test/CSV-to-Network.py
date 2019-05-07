import sys


if len(sys.argv) <=1:
    quit()

drum = {}

drum[36] = 1 #bass drum
drum[41] = drum[43] = drum[45] = drum[47] = drum[48] = drum[50] = 2 #toms
drum[38] = drum[40] = 3 #snares
drum[49] = drum[51] = drum[52] = drum[55] = drum[57] = drum[59] = 4 #cymbals
drum[42] = drum[44] = drum[46] = 5 #Hi-Hat

division = 40
'''
def read_notes(track,fp,line,values):
    notes = []
    while int(values[0]) < track:
        line = fp.readline()
        values = line.split(', ')
        values[-1] = values[-1].strip()
    while int(values[0]) == track:
        while values[2] != "Note_on_c":
            line = fp.readline()
            values = line.split(', ')
            values[-1] = values[-1].strip()
            if int(values[0]) != track:
                break
        start = values[1]
        note = values[4]
        velocity = values[5]
        while values[2] != "Note_off_c" and values[4] != note:
            line = fp.readline()
            values = line.split(', ')
            values[-1] = values[-1].strip()
            if int(values[0]) != track:
                break
        final = values[1]
        notes.append((int(start)//16,int(final)//16,note,velocity))
    return notes

def read_instrument(track,fp,line,values):
    notes = read_notes(track,fp,line,values)
    instrument = [None] * notes[-1][1]
    end = 0
    for note in notes:
        if end < note[0]:
            instrument[end:note[0]] =(0,0,0)
        instrument[note[0]] = (1,note[2],note[3])
        instrument[note[0] + 1:note[1]] = (2,note[2],note[3])
        end = note[1]
    return instrument


'''

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
drums,line,values = read_instrument(2,fp,line,values)
drums = fix_instrument(drums)
#BASS
bass,line,values = read_instrument(3,fp,line,values)
bass = fix_instrument(bass)
#GUITAR
#guitar,line,values = read_instrument(4,fp,line,values)

lent = max(len(drums), len(bass), len(guitar))

for i in range(lent - len(drums)):
    drums.append((0,0,0))
for i in range(lent - len(bass)):
    bass.append((0,0,0))
for i in range(lent - len(guitar)):
    guitar.append((0,0,0))
fp.close()


import os

name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
#os.remove(name + ".txt")
fp = open("../Network-Input/" + name + ".txt", 'w')

cnt = 0

lead = bass

#Only beats
for i in range(len(drums)):
    if drums[i][0] != 1:
        drums[i] = (0,0,0)
    fp.write(str(lead[i][0]) + " "  + str(lead[i][2]) + " " + str(drums[i][0]) + "\n")

#all Values
#for i in range(len(drums)):
#    fp.write(' '.join(map(str,guitar[i][0])) + " " + ' '.join(map(str,guitar[i][1])) + " ")
#    fp.write(' '.join(map(str,bass[i][0])) + " " + ' '.join(map(str,bass[i][1])) + " ")
#    fp.write(' '.join(map(str,drums[i][0])) + " " + ' '.join(map(str,drums[i][1])) + "\n")
#    cnt =cnt+division

fp.close()
