from machine import Pin, Timer
import time
timer = Timer()

led = Pin(15, Pin.OUT)
led2 = Pin(6, Pin.OUT)
led3 = Pin(7, Pin.Out)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

print(button.value())

while True:
    def blink(timer):
        led.toggle()
        time.sleep(0.1)
        led2.toggle()
        time.sleep(0.2)
        led3.toggle()
        time.sleep(0.1)
        
    if button.value():
        timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)