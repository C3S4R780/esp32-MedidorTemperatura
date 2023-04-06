# This file is executed on every boot (including wake-boot from deepsleep)
import network
import json
from time import sleep

net = network.WLAN(network.STA_IF)
net.active(True)
timeout = 0

with open("redesSalvas.json", "r") as file:
    redes = json.load(file)

for rede in redes:
    if net.isconnected(): break
    net.connect(rede["ssid"], rede["password"])

if not net.isconnected():
    while (not net.isconnected() and timeout < 5):
        timeout =+ 1
        sleep(1)
    if timeout == 4: print("Connection timeout.")
