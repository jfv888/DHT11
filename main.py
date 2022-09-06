import RPi.GPIO as GPIO
import dht11
import time
import paho.mqtt.subscribe as subscribe




while True:
    temp = subscribe.simple("sensor/temperature", hostname="10.4.1.127")
    humidity = subscribe.simple("sensor/humidity", hostname="10.4.1.127")
    print("%s %s" % (temp.topic, temp.payload))
    print("%s %s" % (humidity.topic, humidity.payload))
    time.sleep(5)



