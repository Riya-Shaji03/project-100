class Atm(object):
    def __init__(self,atmCard,atmPin):
        self.atmCard = atmCard,
        self.atmPin = atmPin
    def start(self):
        print('started')
    def stop(self):
        print('stopped')
    def withDrawal(self):
        print('withdrawing')
    def deposit(self):
        print('depositing')

user1 = Atm(45738,42746)
user1.start()
print(user1)
