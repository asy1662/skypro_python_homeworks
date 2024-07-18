from smartphone import Smartphone
catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79261234567"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79361234567"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79461234567"))
catalog.append(Smartphone("Google", "Pixel 5", "+79561234567"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")