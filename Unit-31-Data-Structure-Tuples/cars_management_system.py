
# Unit 31 - Data Structures: Tuples
# Demonstration: Car Management System

# Global list of tuples
# Each tuple: (make, model, color, year, owner)
car_lot = [
    ("Toyota", "Tacoma", "Red", 2021, "Isaiah"),
    ("Tesla", "Model S", "Silver", 2026, "Arturo"),
    ("Honda", "Odyssey", "Blue", 2004, "Juaño")
]


def show_menu():
    print("\n===== Car Management System =====")
    print("1. View all cars")
    print("2. Access tuple elements")
    print("3. Add a car")
    print("4. Search for a car")
    print("5. Change a car's color")
    print("6. Remove a car")
    print("7. Exit")


def view_cars():
    if len(car_lot) == 0:
        print("No cars to show")

    for i in range(len(car_lot)):
        car = car_lot[i]
        print(f"{i} - {car}")


def access_tuple(index = 0):
    if 0 <= index < len(car_lot):
        return car_lot[index]

    return None


def add_car():
    make = input("Enter make: ")
    model = input("Enter model: ")
    color = input("Enter color: ")

    try:
        year = int(input("Enter year: "))
    except ValueError:
        year = 0
    
    owner = input("Enter owner: ")

    car_lot.append((make, model, color, year, owner))


def search_car_by_owner():
    owner = input("Enter the owner name: ").lower()

    for index in range(len(car_lot)):
        car = car_lot[index]

        #                   0       1   2       3       4
        # car is a tuple: (make, model, color, year, owner)
        if car[4].lower() == owner:
            return (car, owner)

    return ((), owner)


def change_color(index, color):
    # Get the car tuple at whatever index user chooses
    car = car_lot[index]

    if len(car) == 5:
        # Unpack the tuple (car)
        # Python has discard temporary varible _
        make, model, _, year, owner = car

        # Create the new car with the new color (copy old values)
        new_car = (make, model, color, year, owner)

        # Update the index where old car was with the new one
        car_lot[index] = new_car

    return car


def remove_car(index):
    return car_lot.pop(index)


def main():
    while True:
        show_menu()

        choice = input("\nSelect an option: ")

        if choice == "1":
            view_cars()

        elif choice == "2":
            view_cars()
            print()

            index = int(input("Pick a car to show details: "))

            car = access_tuple(index)

            if car is not None:
                # tuple unpacking
                # Each tuple: (make, model, year, color, owner)
                make, model, year, color, owner = car

                print(  f"Individual Details: " \
                    f"\n\tMake: {make}" \
                    f"\n\tModel: {model}" \
                    f"\n\tColor: {year}" \
                    f"\n\tYear: {color}" \
                    f"\n\tOwner: {owner}")

            else:
                print(f"Car not found for index {index}")


        elif choice == "3":
            add_car()

            print(f"Car Added - ")
            
            # Show the last car
            access_tuple(-1)

        elif choice == "4":
            # Unpack the returned tuple
            car, owner = search_car_by_owner()

            if len(car) == 5:
                make, model, year, color, owner = car

                print(  f"Individual Details: " \
                    f"\n\tMake: {make}" \
                    f"\n\tModel: {model}" \
                    f"\n\tColor: {year}" \
                    f"\n\tYear: {color}" \
                    f"\n\tOwner: {owner}")

            else:
                print(f"Car not found for owner {owner}")


        elif choice == "5":
            # We use this index for validating car found
            index = -1

            # This loop is to get a valid car that exists in the lot
            while True:
                view_cars()

                try:
                    index = int(input("Enter the Index of the Car to change color: "))

                    # Validate index is valid between 0 and < car_lot length
                    if index >= 0 and index < len(car_lot):
                        break

                    print(f"Invalid Index. Please enter a number between 0 and {len(car_lot) - 1}")
                except ValueError:
                    print("Invalid Input. Please enter a valid index")
                    continue

            # Get the Old Color
            old_color = car_lot[index][2]

            # This loop is to ensure we get a color
            while True:
                new_color = input("Enter the new color (red, blue, yellow, white): ").lower()

                # If you really want to validate colors you can do something like this
                real_colors = ("red", "blue", "yellow", "white")

                if not new_color or new_color not in real_colors:
                    print("Color cannot be empty or is not a valid color")
                    continue

                break

            change_color(index, new_color)

            print(f"Color changed from {old_color} to new {new_color}")

        elif choice == "6":
            while True:
                index = int(input(f"Pick a car to remove (0 - {len(car_lot) - 1}): "))
                
                if index >= 0 and index < len(car_lot):
                    removed_car = remove_car(index)
                    print(f"Removed: {removed_car}")
                    break
                else:
                    print(f"Invalid Car Index. Enter between 0 and {len(car_lot) - 1}")

            if removed_car is None:
                print(f"Car could not be removed")

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except InterruptedError:
        print("\nProgram interrupted. Exiting...")
