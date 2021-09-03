from mjremote import mjremote
from random import choice
import time

m = mjremote()
print('Connect: ', m.connect())
b = bytearray(3*m.width*m.height)
t0 = time.time()
while time.time() - t0:
    m.setqpos()
t1 = time.time()
print('FPS: ', 100/(t1-t0))
m.close()