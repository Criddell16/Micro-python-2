from machine import Pin, Timer
import time
timer = Timer()

led = Pin(15, Pin.OUT)
led2 = Pin(6, Pin.OUT)
led3 = Pin(7, Pin.OUT)
led4 = Pin(8, Pin.OUT)
led5 = Pin(9, Pin.OUT)
led6 = Pin(13, Pin.OUT)
button = Pin(14, Pin.IN, Pin.Pull_DOWN)

print(button.value())

while true:
    def blink(timer):
        led.toggle()
        time.sleep(0.1)
        led2.toggle()
        time.sleep(0.1)
        led.toggle()
        time.sleep(0.1)
        led3.toggle()
        time.sleep(0.1)
        led2.toggle()
        time.sleep(0.1)
        led4.toggle()
        time.sleep(0.1)
        led3.toggle()
        time.sleep(0.1)
        led5.toggle()
        time.sleep(0.1)
        led4.toggle()
        time.sleep(0.1)
        led6.toggle()
        time.sleep(0.1)
        led5.toggle()
        time.sleep(0.1)
        led5.toggle()
        time.sleep(0.1)
        led6.toggle()
        time.sleep(0.1)
        led4.toggle()
        time.sleep(0.1)
        led5.toggle()
        time.sleep(0.1)
        led3.toggle()
        time.sleep(0.1)
        led4.toggle()
        time.sleep(0.1)
        led2.toggle()
        time.sleep(0.1)
        led3.toggle()
        time.sleep(0.1)
        
    if button.value():
        timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)