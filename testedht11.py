import machine
import dht
from time import sleep

sensor = dht.DHT11(machine.Pin(4))

while True:
    sensor.measure()
    print("Temperatura = {}".format(sensor.temperature()))
    print("Umidade = {}".format(sensor.humidity()))
    sleep(5)