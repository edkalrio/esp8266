from sht30 import SHT30
import ssd1306
import time

sensor = SHT30()
t, h = sensor.measure()

i2c = machine.I2C(-1, machine.Pin(4), machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text(str(t) + "C", 0, 0)
oled.text(str(h) + "%", 0, 10)
oled.text("RW Labs", 0, 20)
oled.show()

time.sleep(30)
oled.fill(0)
oled.show()