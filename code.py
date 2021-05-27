import time

from launchcontrol import launchcontrol

lc = launchcontrol("PatBoud's Launch Controller")

#lc.ledsInit()

while True:
    lc.scanBtns()

    if (lc.flagPret == True):
        lc.ledFlashPico()

    time.sleep(0.05)
#    lc.ledsInit()
#    time.sleep(1)
#    lc.launch()
#    time.sleep(1)
#    lc.clear()
#    time.sleep(2)
