import sys
import Adafruit_DHT
import time

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    
    t = str(temperature)
    h = str(humidity)
    print (time.ctime())
    print ("temperature: %s C" % t)
    print ("humidity: %s %%" % h)
    # you can write results to file
    #f = open("/home/pi/MagicMirror/modules/Hellloworld/test.txt", "w")
    #f.write("{:s}\ntemperature : {:s} C \nhumidity: {:s} %".format(time.ctime(), t, h))
    #f.flush()
    #f.close
    time.sleep(300)
