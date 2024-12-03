class User:
    age = 18
    def __init__(self, name):
        print('я создался')
        #print('меня зовут ', name)
        self.username = name
    def sayName(self):
        print('меня зовут ', self.username)
    def sayAge(self):
        print(self.age)
    def setAge(self, newAge):
        self.age = newAge
    def addCard(self, card):
        self.card = card
    def getCard(self):
            return self.card 

user1 = User("Petr")
user1.sayName()
user1.sayAge()
user1.setAge(33)
user1.sayAge()