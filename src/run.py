#!/usr/bin/env python3

import vlc
import datetime as dt

triads = [(dt.time(hour = 4 * i), dt.time(hour = (4 * i) + 3, minute = 59, second = 59)) for i in range(6)]
playlist = ["file" + str(i) + ".mp4" for i in range(6)]
#player = vlc.Instance.media_player_new()

while True:
	rn = dt.datetime.now().time()

	if rn > triads[0][0] and rn < triads[0][1]:
		# media playback
		player = vlc.MediaPlayer(playlist[0])
		player.play()
		#media = vlc.Instance.media_new("")
	elif rn > triads[1][0] and rn < triads[1][1]:
		# media Playback
		player = vlc.MediaPlayer(playlist[1])
		player.play()
		#media = vlc.Instance.media_new("")
	elif rn > triads[2][0] and triads[2][1]:
		# media playback
		player = vlc.MediaPlayer(playlist[2])
		player.play()
		#media = vlc.Instance.media_new("")
	elif rn > triads[3][0] and triads[3][1]:
		# media playback
		player = vlc.MediaPlayer(playlist[3])
		player.play()
		#media = vlc.Instance.media_new("")
	elif rn > triads[4][0] and triads[4][1]:
		# media playback
		player = vlc.MediaPlayer(playlist[4])
		player.play()
		#media = vlc.Instance.media_new("")
	elif rn > triads[5][0] and triads[5][1]:
		# media playback
		player = vlc.MediaPlayer(playlist[5])
		player.play()
		#media = vlc.Instance.media_new("")
	else:
		print("[WARN] Somehow out of range")

	#player.set_media(media)
	#player.play()
