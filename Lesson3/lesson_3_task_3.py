from Lesson3.Address import Address
from Lesson3.Mailing import Mailing
to_address = Address("1231312", "Видное", 'Крымская', '5','8')
from_address = Address('231231412', 'Ковылкино', 'Толстого', '24', '1')
mailing = Mailing( to_address, from_address, 400, 'trask987654')
print(mailing)