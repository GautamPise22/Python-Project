from Room import Room  # Adjust the import based on your project structure

def main():
    room = Room(-1)
    
    while True:
        print("\n** Hotel Management System **")
        print("1. Take a Room")
        print("2. Leave a Room")
        print("3. Exit")
        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a numeric option.")
            continue

        if ch == 1:
            room.take_room()  
        elif ch == 2:
            room.leave_room()  
        elif ch == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == '__main__':
    main()