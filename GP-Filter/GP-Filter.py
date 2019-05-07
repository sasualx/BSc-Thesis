import guitarpro
import sys

if len(sys.argv) <=1:
    quit()

song = guitarpro.parse(sys.argv[1])

guitarTracks = []
drumTrack = []
bassTrack = []

new_song_tracks = [None,None,None]
g = 0
b = 0
d = 0
bef = len(song.tracks)
for tr in song.tracks:
    instrument = tr.channel.instrument
    if tr.channel.isPercussionChannel == True:
        new_song_tracks[0] = tr
        d = d + 1
        #print("DRUMS")
    if 33 <= instrument <= 40:
        new_song_tracks[1] = tr
        b = b + 1
        #print("BASS")
    if 25 <= instrument <= 32:
        new_song_tracks[2] = tr
        g = g + 1
        #print("GUITAR")

song.tracks = new_song_tracks
if(d and b and g):
    print("SUCCESS FOR ",sys.argv[1])
    guitarpro.write(song,"../../Filtered-Music-Sheet/" + sys.argv[1])
