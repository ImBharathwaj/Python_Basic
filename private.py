class PrivatePerson():
    def __init__(self, name, privateData):
        self.name = name
        self.__privateData = privateData
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

if __name__ == '__main__':
    usersPrivateData = PrivatePerson('Nothing','Something')
    print(usersPrivateData.__privateData)
