import machine
import dht
import urequests
import uasyncio

rele = machine.Pin(2, machine.Pin.OUT)
sensor = dht.DHT11(machine.Pin(4))
event_loop = uasyncio.get_event_loop()

rele.value(1)
    
async def main():
    while True:

        try: sensor.measure()
        except: continue

        req = urequests.get(
            "https://api.thingspeak.com/update?api_key=30YK09A9EY3SHNGY&field1={}&field2={}"
            .format(
                str(sensor.temperature()),
                str(sensor.humidity())
            )
        )
        req.close()
        await uasyncio.sleep(60)

event_loop.create_task(main())
event_loop.run_forever()
