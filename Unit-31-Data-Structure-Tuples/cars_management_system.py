
# Unit 31 - Data Structures: Tuples
# Demonstration: Car Management System

# Global list of tuples
# Each tuple: (make, model, color, year, owner)
cars = [
    ("Toyota", "Camry", "Silver", 2022, "John"),
    ("Honda", "Civic", "Blue", 2020, "Mary"),
    ("Ford", "Mustang", "Red", 2024, "David")
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
    pass


def access_tuple():
    pass


def add_car():
    pass


def search_car():
    pass


def change_color():
    pass


def remove_car():
    pass


def main():
    while True:
        show_menu()

        choice = input("\nSelect an option: ")

        if choice == "1":
            view_cars()

        elif choice == "2":
            access_tuple()

        elif choice == "3":
            add_car()

        elif choice == "4":
            search_car()

        elif choice == "5":
            change_color()

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
