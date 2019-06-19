#!/usr/bin/env python3

import vlc
import datetime as dt
import os

# Name of Folder containing media files
folder = input("Enter path to directory")
# List of media files
playlist = os.listdir(folder)
# number of media files
n = len(playlist)
# interval difference/gap
d = 24 // n

# actual intervals in dt.time
intervals = [(dt.time(hour = d * i), dt.time(hour = (d * i) + (d - 1), minute = 59, second = 59)) for i in range(n)]

# current time
rn = dt.datetime.now().time()

# index of the media to play based on interval current time lies in
res = list(map(lambda y: rn > y[0] and rn < y[1], intervals)).index(True)

# Instance of VLC Media player loaded with the media file
player = vlc.MediaPlayer(playlist[res])
# playing the media file
player.play()
