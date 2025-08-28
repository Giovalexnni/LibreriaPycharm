from tkinter.font import names

class User:
    def __init__(self, id, name, phone, mail):
        self._id = id
        self._name = name
        self._phone = phone
        self._mail = mail

    @property
    def id(self): return self._id
    @id.setter
    def id(self, id): self._id = id

    @property
    def name(self): return self._name
    @name.setter
    def name(self, name): self._name = name

    @property
    def phone(self): return self._phone
    @phone.setter
    def phone(self, phone): self._phone = phone

    @property
    def mail(self): return self._mail
    @mail.setter
    def mail(self, mail): self._mail = mail


class Friend(User):
    def __init__(self, id, name, phone, mail, address, rol):
        super().__init__(id, name, phone, mail)
        self._address = address
        self._rol = rol

    @property
    def address(self): return self._address
    @address.setter
    def address(self, address): self._address = address

    @property
    def rol(self): return self._rol
    @rol.setter
    def rol(self, rol): self._rol = rol

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "mail": self.mail,
            "address": self.address,
            "rol": self.rol
        }


# Ejemplo de uso (sin input dentro de clases)
friends = {}
for i in range(3):
    id = int(input("ID Amigo: "))
    name = input("Nombre Amigo: ")
    phone = input("Teléfono: ")
    mail = input("Email: ")
    address = input("Dirección: ")
    rol = input("Rol: ")

    f = Friend(id, name, phone, mail, address, rol)
    friends[f.id] = f.to_dict()

print(friends)
