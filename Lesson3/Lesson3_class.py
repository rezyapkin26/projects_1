from Lesson3.user import User
from Lesson3.card import Card

user1 = User("Petr")
user1.sayName()
user1.sayAge()
user1.setAge(33)
user1.sayAge()

card = Card('3454 1234 5678 7890', '11/28','Petr R' )
#card.pay(1000)
user1.addCard(card)
user1.getCard().pay(1000)
