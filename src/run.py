#!/usr/bin/env python3

import vlc
import datetime as dt
import os

folder = input("Enter path to directory")
playlist = os.listdir(folder)
n = len(playlist)
d = 24 // n
intervals = [(dt.time(hour = d * i), dt.time(hour = (d * i) + (d - 1), minute = 59, second = 59)) for i in range(n)]

rn = dt.datetime.now().time()

res = list(map(lambda y: rn > y[0] and rn < y[1], intervals)).index(True)

player = vlc.MediaPlayer(playlist[res])
player.play()
