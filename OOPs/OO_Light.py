class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def show(self):
        print(self.switchIsOn)


if __name__ == '__main__':
    l1 = LightSwitch()
    l1.turnOn()
    l1.turnOff()
    l1.show()
