# -*- coding: utf-8 -*-
from gps3.agps3threaded import AGPS3mechanism
import time
import os
from measurement.measures import Distance



agps_thread = AGPS3mechanism()
agps_thread.stream_data()
agps_thread.run_thread()



while 1:
	callsign = "DL3KB" #change to your callsign

	time.sleep(10) #change to your prefered interval
	dlat = agps_thread.data_stream.lat
	dlon = agps_thread.data_stream.lon
	
	if dlat == "n/a":
		continue
		
	is_positive = dlat >= 0
	dlat = abs(dlat)
	minuteslat,secondslat = divmod(dlat*3600,60)
	degreeslat,minuteslat = divmod(minuteslat,60)
	degreeslat = degreeslat if is_positive else -degreeslat
	

	is_positive = dlon >= 0
	dlon = abs(dlon)
	minuteslon,secondslon = divmod(dlon*3600,60)
	degreeslon,minuteslon = divmod(minuteslon,60)
	degreeslon = degreeslon if is_positive else -degreeslon

	intlatdd = int(round(degreeslat))
	intlatmm = int(round(minuteslat))
	intlathh = round ((secondslat/60)*100)
	intlonhhdec = int (intlathh)
	latdd = '{:02d}'.format(intlatdd)
	latmm = '{:02d}'.format(intlatmm)
	lathh = '{:02d}'.format(intlathhdec)

              


	intlondd = int(round(degreeslon))
	intlonmm = int(round(minuteslon))
	intlonhh = round ((secondslon/60)*100)
	intlonhhdec = int (intlonhh)
	londd = '{:03d}'.format(intlondd)
	lonmm = '{:02d}'.format(intlonmm)
	lonhh = '{:02d}'.format(intlonhhdec)
	
	
	if dlon > 0.0:
	orient_lon = 'E'
	if dlon < 0.0:
	orient_lon = 'W'
	
	if dlat > 0.0:
	orient_lat = 'N'
	if dlat < 0.0:
	orient_lat = 'S'
	
	
	 

	speedkm = (agps_thread.data_stream.speed)
	intknots = (int(round(0.539957 * speedkm)))
	knot3digits = '{:03d}'.format(intknots)
	course = agps_thread.data_stream.track

	lat = '{}{}.{}'.format(latdd, latmm, lathh)
	lon = '{}{}.{}'.format(londd, lonmm, lonhh)
	altgps = agps_thread.data_stream.alt
	alt = int(Distance(m=altgps).ft)
	intalt = int (round(alt))
	alt6digits = '{:06d}'.format(intalt)
	aprs = 'aprs -c {} -o packet.wav "!{}{}/{}{}>{}/{}/A={}"'.format(callsign,lat,orient_lat,lon,orient_lon,course,knot3digits,alt6digits) #I saved the audio into a file, because the pi had some problems with the audio playback
	os.system (aprs)
	aplay = 'sudo aplay -D plughw:0,0 packet.wav'
	os.system (aplay) #play the audio file

		
