from Lesson3.smartphone import smartphone
catalog = []
catalog.append(smartphone('Samsung', 'galaxy M31', '+79998887766'))
catalog.append(smartphone('Nokia', 'cirpich', '+79997776655'))
catalog.append(smartphone('Siemens', ' C65', '+79996665544'))
catalog.append(smartphone('Motorola', 'ZXW', '+79995554433'))
catalog.append(smartphone('Apple', 'Iphone 15', '+79994443322'))
for smartphone in catalog:
    print(f"<{smartphone.make}> - <{smartphone.model}> - <{smartphone.number_phone}>")