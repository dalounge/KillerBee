

import csv

path = 'c:\\wapsie\\music.csv'
music_list = {} # this naming is too long and not pythonic.  name it nicer, normally 2 words or less

with open(path, 'r', encoding = 'UTF-8') as music: # You should put the path in a variable so that you only have to change it in one place
    reader = csv.reader(music)
    for band, album, song in reader: # each part that you add to a for reads that column.  much easier
        if band not in music_list:
            music_list[band] = {}

        if album: # if album what? no need for this line. if you are error catching it would fail anyways.
            if album not in music_list[band]:
                music_list[band][album] = []
            music_list[band][album].append(song)
    print(music_list)
    
import csv
path = 'c:\\wapsie\\music.csv'
music_list = {}

class Discography:
    def __init__(self):
        self.albums = {}

with open(path, 'r', encoding='UTF-8') as f:
    c = csv.reader(f)
    
    for band, album, song in c:
        if band not in music_list:
            disc = Discography()
            music_list[band] = disc
            
        if album not in music_list[band].albums:
            music_list[band].albums[album] = []
            
        music_list[band].albums[album].append(song)
        
print(music_list['52 Commercial Road'].albums['52 Commercial Road - 52 Commercial Road'])
            
        
