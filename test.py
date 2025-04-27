from machine import Pin
import time


TRIG_PIN = 5
ECHO_PIN = 18
LED_PIN = 23


trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)


def measure_distance():
    
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    
    
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
    
    
    duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (duration * 0.0343) / 2  
    return distance


while True:
    dist = measure_distance()
    print("Distance:", dist, "cm")
    if dist < 30:  
        led.on()  
        print("Intruder detected!")
    else:
        led.off()
    time.sleep(0.5)




