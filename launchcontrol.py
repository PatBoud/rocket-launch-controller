#launchcontrol.py
import time
import board
import digitalio


class launchcontrol():

    def __init__ (self, name = ""):
        self.name = name
        print ("------------------------------------------")
        print ("----- " + name + " -----")
        print ("------------------------------------------")
        print ("")
        print ("Initialisation du controleur")
        print ("..........................................")
        print ("")
        print("Initialisation des leds...")
        self.ledPico = digitalio.DigitalInOut(board.LED)
        self.ledPico.direction = digitalio.Direction.OUTPUT

        self.ledMain = digitalio.DigitalInOut(board.GP0)
        self.ledMain.direction = digitalio.Direction.OUTPUT

        self.ledMeteo = digitalio.DigitalInOut(board.GP1)
        self.ledMeteo.direction = digitalio.Direction.OUTPUT

        self.ledZone = digitalio.DigitalInOut(board.GP2)
        self.ledZone.direction = digitalio.Direction.OUTPUT

        self.ledArm = digitalio.DigitalInOut(board.GP3)
        self.ledArm.direction = digitalio.Direction.OUTPUT

        self.ledArm = digitalio.DigitalInOut(board.GP4)
        self.ledArm.direction = digitalio.Direction.OUTPUT

        self.ledContA = digitalio.DigitalInOut(board.GP5)
        self.ledContA.direction = digitalio.Direction.OUTPUT

        self.ledContB = digitalio.DigitalInOut(board.GP6)
        self.ledContB.direction = digitalio.Direction.OUTPUT

        self.ledPretA = digitalio.DigitalInOut(board.GP7)
        self.ledPretA.direction = digitalio.Direction.OUTPUT

        self.ledPretB = digitalio.DigitalInOut(board.GP8)
        self.ledPretB.direction = digitalio.Direction.OUTPUT

        print("Initialisation des boutons...")
        self.btn1 = digitalio.DigitalInOut(board.GP15)
        self.btn1.pull = digitalio.Pull.UP
        self.btn1_prevState = self.btn1.value


        print("Initialisation des relais...")
        self.relaisA = digitalio.DigitalInOut(board.GP16)
        self.relaisA.direction = digitalio.Direction.OUTPUT
        self.relaisA.value = True

        self.relaisB = digitalio.DigitalInOut(board.GP17)
        self.relaisB.direction = digitalio.Direction.OUTPUT
        self.relaisB.value = True

        print("Initialisation des variables...")
        self.clearFlags()

        print ("------------------------------------------")
        print ("Initialisation complétée")
        print ("==========================================")
        print ("")


    def getName(self):
        return (self.name)

    def ledsInit(self):
        print("")
        print("LEDS INIT")
        self.ledFlash(self.ledPico, 0.5, 3)

        self.ledPico.value = True
        time.sleep(0.2)
        self.ledMain.value = True
        time.sleep(0.5)
        self.ledMeteo.value = True
        time.sleep(0.5)
        self.ledZone.value = True
        time.sleep(0.5)

        self.flagPret = True


    def ledFlash(self, led, delais, nbFois = 1):
        for i in range(nbFois):
            led.value = True
            time.sleep(delais)
            led.value = False
            time.sleep(delais)

    def ledFlashPico(self):
        self.ledFlash(self.ledPico, 0.1)

    def launch(self, fuseeA = True, fuseeB = False):
        print("")
        print ("!!!!!! LAUNCH !!!!!!")
        self.ledFlash(self.ledPico, 0.05, 20)

        self.clearLeds()
        self.relaisA.value = not fuseeA
        self.relaisB.value = not fuseeB

        time.sleep(3)

        self.relaisA.value = True
        self.relaisB.value = True

        time.sleep(0.5)

        self.ledFlash(self.ledPico, 0.2, 3)

    def clear(self):
        print ("CLEAR")
        self.clearFlags()
        self.clearLeds()
        self.clearRelais()


    def clearLeds(self):
        self.ledPico.value = False
        self.ledMain.value = False
        self.ledMeteo.value = False
        self.ledZone.value = False

    def clearRelais(self):
        self.relaisA.value = True
        self.relaisB.value = True

    def clearFlags(self):
        self.flagMeteo = False
        self.flagZone = False
        self.flagArm = False
        self.flagContA = False
        self.flagContB = False
        self.flagPret = False

    def scanBtns(self):
        if (self.btn1.value != self.btn1_prevState):
            if (self.btn1.value == False):
                if(self.flagPret == True):
                    self.launch()
                    self.clear()
                else:
                    self.ledsInit()

        self.btn1_prevState = self.btn1.value

