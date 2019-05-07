

fp = open("AC-DC - The Jack (3).csv","r")

dr = open("result.txt","r")

res = open("result.csv","w")

line = fp.readline()
while(int(line[0])<2):
    res.write(line)
    line = fp.readline()
values = line.split(', ')
values[-1] = values[-1].strip()

while(values[2]!="Note_on_c"):
    res.write(line)
    line = fp.readline()
    values = line.split(', ')
    values[-1] = values[-1].strip()

while values[2]!= "End_track":
    line = fp.readline()
    values = line.split(', ')
    values[-1] = values[-1].strip()

line = dr.readline()
while line:
    res.write(line)
    line = dr.readline()

line = fp.readline()
while line:
    res.write(line)
    line = fp.readline()

fp.close()
dr.close()
res.close()
