from gpiozero import LightSensor, LED
from time import sleep

light = LightSensor(4, charge_time_limit=0.001)
buzzer = LED(26)

buzzer.off()
sleep(1)

light.wait_for_dark()
buzzer.on()
