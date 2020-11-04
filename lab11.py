from machine import ADC,SPI,PWM,Pin
import time,network
import BlynkLib

sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("colombo0718", "12345678")
while not sta_if.isconnected():
    pass
print('wifi connect')

token="s8UalOzfOY-Cex91g8gZdgFPcgaYc7_2"
blynk=BlynkLib.Blynk(token)

# light A0
light = ADC(0)

# laser D6
laser=Pin(12,Pin.OUT)
laser.value(1)

while True :
    print(light.read(),laser.value()==1)
    if light.read() < 200 and laser.value()==1 :
        print('外面有人喔')
        blynk.notify("外面有人喔")
    time.sleep(1)

