# Define custom exceptions
class AadharException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RoomException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PhoneException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Room:
    # Class attributes: initialize a list with 51 elements (index 0 unused for simplicity)
    roomnumber = [None] * 51  
    roomType = None

    def __init__(self, val):
        # Fill the roomnumber list with the given value (for indices 0 through 50)
        for i in range(len(Room.roomnumber)):
            Room.roomnumber[i] = val

    @staticmethod
    def length(str_val, k):
        """
        Check if the string's length is exactly k and if it contains at least one digit.
        """
        if len(str_val) == k:
            for ch in str_val:
                if ch.isdigit():
                    return True
        return False

    def take_room(self):
        try:
            # Open the file in append mode (adjust the file path as necessary)
            with open("records.txt", "a") as bWriter:
                name = input("Enter Customer Name: ")
                identity = input("Enter Customer Identity Number (Aadhar Card): ")
                if not Room.length(identity, 12):
                    raise AadharException("Enter valid Aadhar Card Number.")
                phone_number = input("Enter Customer Phone Number: ")
                if not Room.length(phone_number, 10):
                    raise PhoneException("Enter valid Phone Number.")
                room_type = input("Enter Room Type (AC/Non-AC): ")
                Room.roomType = room_type  # Set the class attribute
                room_charge_per_day = 0.0
                if room_type.lower() == "ac":
                    room_charge_per_day = 2000.0
                elif room_type.lower() == "non-ac":
                    room_charge_per_day = 1000.0
                else:
                    raise RoomException("Enter valid Room Type.")
    
                number_of_days = int(input("Enter Number of Days to Stay: "))
    
                # Write the record details to file
                bWriter.write(" " + name)
                bWriter.write(" " + identity)
                bWriter.write(" " + phone_number)
                bWriter.write(" " + room_type)
                bWriter.write(" " + str(number_of_days))
                bWriter.write("\n")
    
                # Import Bill from your bill module (adjust the module name as needed)
                from Bill import Bill
                bill = Bill(name, identity, phone_number, room_type, room_charge_per_day, number_of_days)
                print("\n** Bill Details **")
                bill.print_bill()
        except AadharException as ex1:
            print("Error:", ex1)
        except RoomException as ex2:
            print("Error:", ex2)
        except PhoneException as ex3:
            print("Error:", ex3)
        except IOError as ex4:
            print(ex4)

    def leave_room(self):
        room = int(input("Enter Room Number to Leave: "))
        if Room.roomnumber[room] == -1:
            print("Room", room, "is already vacant! Please try a valid Room Number")
        else:
            print("Room", room, "has been vacated. Thank you!")
            Room.roomnumber[room] = -1

    @staticmethod
    def room_number():
        """
        Assigns and returns a vacant room number based on the room type.
        For 'AC' rooms, room numbers 1-25 are used.
        For 'Non-AC' rooms, room numbers 26-50 are used.
        """
        if Room.roomType and Room.roomType.lower() == "ac":
            for i in range(1, 26):  # 1 to 25 inclusive
                if Room.roomnumber[i] == -1:
                    Room.roomnumber[i] = i
                    return i
        elif Room.roomType and Room.roomType.lower() == "non-ac":
            for i in range(26, 51):  # 26 to 50 inclusive
                if Room.roomnumber[i] == -1:
                    Room.roomnumber[i] = i
                    return i
        return -1


