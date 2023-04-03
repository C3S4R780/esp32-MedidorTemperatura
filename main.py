# import esptool
import machine
from time import sleep

rele = machine.Pin(2, machine.Pin.OUT)
i = 0
while (i < 5):
    rele.value(1)
    sleep(1)
    rele.value(0)
    sleep(1)
    i += 1