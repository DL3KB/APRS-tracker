# APRS-tracker
An software only APRS tracker, using AFSK together with python.

Just feed the audio from your Raspberry Pi (or something similar) into a transmitter. 

Made possible with a program called AFSK. (https://github.com/casebeer/afsk.git)




Setup: 
1. install gpsd
2. bind your GPS receiver to a gpsd socket
3. install python gps (https://github.com/wadda/gps3)
4. install afsk (https://github.com/casebeer/afsk.git)
5. change the parameters in tracker.py 
6. connect your Pi (or an equivalent) to your transmitter via a audio cable 
