from machine import Pin
import utime

led = Pin(25, Pin.OUT)
delay = 1

while True:
        led.high()
        utime.sleep(delay)
        led.low()
        utime.sleep(delay)
        



