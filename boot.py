# This file is executed on every boot (including wake-boot from deepsleep)
import network
import json
from time import sleep

net = network.WLAN(network.STA_IF)
net.active(True)

with open("redesSalvas.json", "r") as file:
    redes = json.load(file)

while not net.isconnected():
    for rede in redes:
        if net.isconnected(): break
        net.connect(rede["ssid"], rede["password"])
        sleep(5)
