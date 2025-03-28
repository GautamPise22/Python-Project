from Hotel import Hotel
from Room import Room

class Bill(Hotel):
    def __init__(self, name, identity, phoneNumber, roomType, roomChargePerDay, number_of_days):
        super().__init__(name, identity, phoneNumber, roomType, roomChargePerDay)
        self.number_of_days = number_of_days

    def calculate_bill(self, number_of_days):
        room_charge = self.roomChargePerDay * number_of_days
        gst = 0.18
        total_bill = room_charge + (room_charge * gst)
        return total_bill

    def print_bill(self):
        total_bill = self.calculate_bill(self.number_of_days)
        print("Customer Name:", self.name)
        print("Customer Aadhar Card Number:", self.identity)
        print("Customer Phone Number:", self.phoneNumber)
        print("Room Type:", self.roomType)
        print("Room Number:", Room.room_number())
        print("Room Charge Per Day: ₹", self.roomChargePerDay)
        print("Number of Days:", self.number_of_days)
        print("Room Charge: ₹", self.roomChargePerDay * self.number_of_days)
        print("GST (18%): ₹", (self.roomChargePerDay * self.number_of_days) * 0.18)
        print("Total Bill (including GST): ₹", total_bill)

        with open("records.txt", "a") as bWriter:
            bWriter.write(" " + str(Room.room_number()-1))
            bWriter.write(" " + str(total_bill))

