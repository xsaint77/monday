from sense_hat import SenseHat
import os
import blinkpy

red = (255, 0, 0)
green = (0,255,0)
purple = (128,0,128)
blue = (0,0,128)
sense = SenseHat()
while True:
    sense.clear
    temp = round(sense.get_temperature(), 2)
    farhrenheit = round(((temp/5)*9)+32, 2)
    print(farhrenheit)
    print(temp)
    message=str(farhrenheit)
    if farhrenheit >178:
        bg = red
        sense.show_message(message, scroll_speed=.1, back_colour=bg, text_colour=blue)
        os.system("sudo python device.py -e a17sl83582h7nm-ats.iot.us-west-2.amazonaws.com -r /home/pi/certs/root.ca.pem -c /home/pi/certs/ea189445df.cert.pem -k /home/pi/certs/ea189445df.private.key")
        
    else:
        bg = blue
        sense.show_message(message, scroll_speed=.1, back_colour=bg, text_colour=red)
        
