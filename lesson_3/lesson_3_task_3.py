from adress import Address
from mailing import Mailing

from_address = Address("123456", "Москва", "Кронштадтский бульвар", "30", "15")
to_address = Address("654321", "Санкт-Петербург", "Невский проспект", "40", "25")

mailing = Mailing(to_address, from_address, 350, "TRACK12345678")

print(mailing)