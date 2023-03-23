class Package():

    def __init__(self, 
                 id=0, 
                 weight=1.0, 
                 description="Description",
                 W_GR_100 = 10,
                 cost=1.0):
        self._id = 0 if id == None else id
        self._weight = 1 if weight == 0 else weight
        self._description = 'description' if 'description' == None else description
        self._cost = 1.0 if cost == 0.0 else cost

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = 0 if id == None else id

    def get_weight(self, weight):
        return self._weight

    def set_weight(self, weight):
        self._weight = 1 if weight == 0 else weight

    def set_description(self, description):
        self._description = 'description' if 'description' == None else description

    def get_description(self):
        return self._description

    def set_cost(self, cost):
        self._cost = 1.0 if cost == 0.0 else cost

    def get_cost(self):
        return self._cost

    def calculate(self):
        print(f"Costo total de envio: ${self._description}",
              self._cost * self._weight)


class StandardPackage(Package):

    def __init__(self,
                 id=0,
                 weight=1.0,
                 description="Description",
                 cost=1.0,
                 overweight=1.0,
                 fixedfee=1.0):
        super().__init__(id, weight, description, cost)
        self.__fixedfee = 1.0 if fixedfee == 0.0 else fixedfee

    def calculate(self):
        print(f"Costo total de envío estandar: ${self.__description}",
              (self.__fixedfee + self.__cost) * self.__weight)


class OverWeightPackage(Package):

    def __init__(self,
                 id=0,
                 weight=1.0,
                 description="Description",
                 cost=1.0,
                 overweight=1.0):
        super().__init__(id, weight, description, cost)
        self.__overweight = 1.0 if overweight == 0.0 else overweight

    def calculate(self):
        print(f"Costo total de envio por sobrepeso: ${self.__description}",
              (self.__overweight + self.__overweight) * self.__cost)


class Person():

    def __init__(self, name="name", lastname="lastname", dni=0, phone=0):
        self._name = "name" if name == None else name
        self._lastname = "lastname" if lastname == None else lastname
        self._dni = 0 if dni == None else dni
        self._phone = 0 if phone == None else phone

    def set_name(self, name):
        self._name = "name" if name == None else name

    def get_name(self):
        return self._name

    def set_last_name(self, lastname):
        self._lastname = "lastname" if lastname == None else lastname

    def get_last_name(self):
        return self._lastname

    def set_dni(self, dni):
        self._dni = 0 if dni == None else dni

    def get_dni(self):
        return self._dni

    def set_phone(self, phone):
        self._phone = 0 if phone == None else phone

    def get_phone(self):
        return self._phone


class Address():

    def __init__(self, address="adress"):
        self.__address = "adress" if address == None else address

    def set_address(self, address):
        self.__address = 0 if address == None else address

    def get_address(self):
        return self.__address

class Delivery(Person,Address):

    def __init__(self,
                 id=0,
                 date='00/00/00',
                 time='00:00',
                 sender=Person(),
                 receiver=Person(),
                 sender_add=Address(),
                 receiver_add=Address(),
                 contact=Person(),
                 items=[Package()]):

        self.__id = 0 if id == None else id

        self.__date = "00/00/00" if date == None else date
        self.__time = "00:00" if time == None else time
        self.__sender = Person() if sender == None else sender
        self.__receiver = Person() if receiver == None else receiver

        self.__sender_add = Address() if sender_add == None else sender_add
        self.__receiver_add = Address() if receiver_add == None else receiver_add
        self.__contact = Person() if contact == None else contact
        self.__items = [Package()] if items == None else items

    def set_id(self, id):
        self.__id = 0 if id == None else id

    def get_id(self):
        return self.__id

    def set_date(self, date):
        self.__date = "00/00/00" if date == None else date

    def get_date(self):
        return self.__date

    def set_time(self, time):
        self.__time = "00:00" if time == None else time

    def get_time(self):
        return self.__time

    def set_sender(self, sender):
        self.__sender = Person( ) if sender == None else sender

    def get_sender(self):
        return self.__sender

    def set_receiver(self, receiver):
        self.__receiver = Person() if receiver == None else receiver

    def get_receiver(self):
        return self.__receiver

    def set_sender_add(self, sender_add):
        self.__sender_add = Address() if sender_add == None else sender_add

    def get_sender_add(self):
        return self.__sender_add

    def set_receiver_add(self, receiver_add):
        self.__receiver_add = Address() if receiver_add == None else receiver_add

    def get_receiver_add(self):
        return self.__receiver_add

    def set_contact(self, contact):
        self.__contact = Person() if contact == None else contact

    def get_contact(self):
        return self.__contact

    def set_items(self, items):
        self.__items = [Package] if items == None else items

    def get_items(self):
        return self.__items


#Prueba de codigo
Vendedor = Person('Maryuris', 'Serpa', 1007139116, 3005962760)
Cliente = Person('Camilo', 'Villareal', 1045494348, 3106564526)
Direccion = Address('San Jose')

Paquete = []
Compra = Package(1,50,"Coca Cola",5000)

Paquete.append(Compra)

Entrega = Delivery(64505, "23/03/2023", '10:00', Vendedor, Cliente, Direccion, Direccion, Cliente, Compra)

print("|| Pruebas - Codigo ||\n")
print("Detalles de compra: ")
print("Emisor: ", Entrega.get_sender().get_name())
print("Receptor: ", Entrega.get_receiver().get_name())
print("Direccion:", Direccion.get_address())
print("Producto:", Compra.get_description())


