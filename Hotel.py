from Customer import Customer

class Hotel(Customer):
    def __init__ (self,  name,  identity,  phoneNumber,  roomType,  roomChargePerDay):
        super().__init__(name, identity, phoneNumber)
        self.roomType = roomType
        self.roomChargePerDay = roomChargePerDay
    