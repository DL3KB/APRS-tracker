# APRS-tracker
An software only APRS tracker, using AFSK together with python.

Just feed the audio from your Raspberry Pi (or something similar) into a transmitter. 

Made possible with a program called AFSK. (https://github.com/casebeer/afsk.git)




Setup: 
1. install gpsd
2. bind your GPS receiver to a gpsd socket
3. install python gps (https://github.com/wadda/gps3) ---> "sudo pip3 install gps3"
4. install afsk (https://github.com/casebeer/afsk.git) ---> "sudo pip3 install afsk"
5. install measurement (https://github.com/coddingtonbear/python-measurement) ---> "sudo pip3 install measurement==2.0.1"
6. change the parameters in aprs.py
7. connect your Pi (or an equivalent) to your transmitter via a audio cable and turn on VOX
