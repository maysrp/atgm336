# atgm336
micropython ATGM336 GPS models [ESP32 RP2040]

```
from atgm336 import gps
from machine import UART
import time

uart=UART(0,9600)
g=gps(uart)

while True:
  m=g.gps()
  time.sleep(0.1)
```
