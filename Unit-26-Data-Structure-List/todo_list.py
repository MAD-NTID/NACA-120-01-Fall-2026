# Define the list variable outside of all functions 
todo_list = []

def add(item):
    todo_list.append(item)

def remove(item_num):
    # Validate Item Number is Within List Length
    # This is human number validation
    if item_num >= 1 and item_num <= len(todo_list):
        removed_item = todo_list.pop(item_num - 1)
        print(f"'{removed_item}' was removed")
    else:
        print("Invalid Item")

def update(item_num):
    if item_num >= 1 and item_num <= len(todo_list):
        item_to_update = todo_list[item_num - 1]
        print(f"'{item_to_update}' to be updated")

        updated_item = input("Enter Update Value: ")

        if updated_item == None or updated_item == "":
            print("Invalid Value - Update Canceled")
            return

        todo_list[item_num - 1] = updated_item
        print(f"Item updated from '{item_to_update}' to '{updated_item}'")
    else:
        print("Invalid Item")

def view():
    # if there's nothing in the todo list, why run the loop?
    # from a user perspective, what should the output be if there
    # is nothing in the list?
    if len(todo_list) == 0:
        print("There's nothing to show")
        return

    # get the len of the list
    # this becomes the range of the for loop
    print("Items in ToDo List: ")
    for index in range(len(todo_list)):
        # index is 0 based (for human reading do plus 1 for listing)
        # leave index as is for actually getting from the list
        print(f"{index + 1} - {todo_list[index]}")

def main():
    print("Welcome to your ToDo List App")

    while(True):
        # \n means new line
        # \t means tab spacing
        print("Todo: \n\t"
              "1. Add \n\t"
              "2. Remove\n\t" 
              "3. Update\n\t" 
              "4. View\n\t" 
              "5. Quit")        

        option = input("Choose Option: ")
        if option == "1":
            item = input("Enter Item to Add: ")

            add(item)

            print(f"Your item '{item}' has been added")
        elif option == "2":
            view()

            if len(todo_list) > 0:
                try:
                    item_num = int(input("Select an Item Number to Remove: "))
                    
                    remove(item_num)
                except ValueError:
                    print("Invalid Item Number Selection")

        elif option == "3":
            view()

            if len(todo_list) > 0:
                try:
                    item_num = int(input("Select an Item Number to Update: "))
                    
                    update(item_num)
                except ValueError:
                    print("Invalid Item Number Selection")
        elif option =="4":
            view()
        elif(option == "5"):
            print("Thank you for using Todo List App")
            break
        else:
            print("Invalid Option\n")

        print()

if __name__ == "__main__":
    main()