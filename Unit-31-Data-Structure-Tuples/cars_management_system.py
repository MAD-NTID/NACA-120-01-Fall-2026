
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
    for car in car_lot:
        print(car)


def access_tuple(index = 0):
    if len(car_lot) > 0 and index <= len(car_lot):
        car = car_lot[index]
        print(car)
        print(  f"Individual Details: " \
                f"\n\tMake: {car[0]}" \
                f"\n\tModel: {car[1]}" \
                f"\n\tColor: {car[2]}" \
                f"\n\tYear: {car[3]}" \
                f"\n\tOwner: {car[4]}")
    else:
        print("Car not found")



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
            return owner

    return None


def change_color(owner):
    for index in range(len(car_lot)):
        car = car_lot[index]

        #                   0       1   2       3       4
        # car is a tuple: (make, model, color, year, owner)
        if car[4].lower() == owner:
            print(f"Current color is: {car[2]}")

            new_color = input("Enter new color: ")

            # Tuple is immutable so create a new one and copy the old values
            car_lot[index] = (car[0], car[1], new_color, car[3], car[4])
            break


def remove_car():
    view_cars()

    index = int(input(f"Pick a car to remove (1 - {len(car_lot)}): "))

    if index >= 1 and index <= len(car_lot):
        print(f"Removed: {car_lot.pop(index - 1)}")


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

            access_tuple(index)

        elif choice == "3":
            add_car()

            print(f"Car Added - ")
            
            # Show the last car
            access_tuple(-1)

        elif choice == "4":
            owner = search_car_by_owner()
            
            if owner is None:
                print(f"Cars not found for owner")

        elif choice == "5":
            view_cars()

            owner = input("Enter the owner name: ").lower()

            change_color(owner)

            view_cars()

        elif choice == "6":
            remove_car()

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
