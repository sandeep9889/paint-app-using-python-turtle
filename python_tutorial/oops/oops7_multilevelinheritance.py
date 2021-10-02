#here is example of multil;evel inheritence
class electronicdevice:
    time ="10hr"
    memory = "1tb"

class pocketdevice(electronicdevice):
    size =150
    charger = "65wat"
    time = "5hr"
class phone(pocketdevice):
    price = 15000
    ram ="8gb"


lenevo = electronicdevice()
tab = pocketdevice()
jio= phone()

print(phone.time)