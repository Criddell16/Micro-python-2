from machine import Pin, PWM, ADC
from time import sleep

pwm = PWM(Pin(15))
pwm2 = PWM(Pin(14))
pwm3 = PWM(Pin(13))
pwm4 = PWM(Pin(12))
pwm5 = PWM(Pin(11))
pwm6 = PWM(Pin(10))

adc = ADC(Pin(26))

pwm.freq(1000)
pwm2.freq(1500)
pwm3.freq(2000)
pwm4.freq(2500)
pwm5.freq(3000)
pwm6.freq(3500)

while True:
    #print(adc.read_u16())
    duty = adc.read_u16()
    pwm.duty_u16(duty)
    pwm2.duty_u16(duty)
    pwm3.duty_u16(duty)
    pwm4.duty_u16(duty)
    pwm5.duty_u16(duty)
    pwm6.duty_u16(duty)
