import machine
import dht
import urequests
import uasyncio

rele = machine.Pin(2, machine.Pin.OUT)
sensor = dht.DHT11(machine.Pin(4))
event_loop = uasyncio.get_event_loop()
    
async def main():
    while True:

        try: sensor.measure()
        except: continue
        
        rele.value(1)

        req = urequests.get(
            "https://api.thingspeak.com/update?api_key=30YK09A9EY3SHNGY&field1={}&field2={}"
            .format(
                str(sensor.temperature()),
                str(sensor.humidity())
            )
        )

        if req.status_code == 200:
            rele.value(0)

        req.close()

        await uasyncio.sleep(60)

event_loop.create_task(main())
event_loop.run_forever()
