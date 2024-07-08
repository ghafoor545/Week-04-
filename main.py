# Import necessary modules and classes
import datetime
from module import FoodItem, Inventory  # Importing FoodItem and Inventory classes from module

# Function to get user input for adding a food item
def get_food_item_input():
    # Prompt user for input
    name = input("Enter food name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))
    barcode = input("Enter barcode: ")
    expiry_date_str = input("Enter expiry date (YYYY-MM-DD): ")
    
    # Convert expiry date string to datetime object
    expiry_date = datetime.datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
    
    # Return a new FoodItem object with user-provided data
    return FoodItem(name, category, quantity, barcode, expiry_date)

# Main execution block
if __name__ == "__main__":
    # Initialize an Inventory instance with the specified CSV file path
    inv = Inventory(filename='/Users/cv/Downloads/Task 04/Inventory.csv')

    # Menu for user interaction
    while True:
        print("\nMenu:")
        print("1. Add a food item")
        print("2. Edit a food item")
        print("3. Search for a food item")
        print("4. Delete a food item")
        print("5. Display inventory")
        print("6. Display near expiry items")
        print("7. Exit")

        # Prompt user to enter their choice
        choice = input("Enter your choice: ")

        # Perform actions based on user's choice
        if choice == "1":
            # Add a new food item to the inventory
            food_item = get_food_item_input()
            inv.add_food_item(food_item)
        elif choice == "2":
            # Edit an existing food item in the inventory
            barcode = input("Enter barcode of item to edit: ")
            food_item = get_food_item_input()
            inv.edit_food_item(barcode, food_item.name, food_item.category, food_item.quantity, food_item.expiry_date)
        elif choice == "3":
            # Search for a food item by its barcode
            barcode = input("Enter barcode of item to search: ")
            item = inv.search_food_item(barcode)
            if item:
                print("Found item:")
                print(item)
            else:
                print("Item not found.")
        elif choice == "4":
            # Delete a food item from the inventory
            barcode = input("Enter barcode of item to delete: ")
            if inv.delete_food_item(barcode):
                print("Item deleted successfully.")
            else:
                print("Item not found for deletion.")
        elif choice == "5":
            # Display the current inventory
            inv.display_inventory()
        elif choice == "6":
            # Display items that are near expiry within 7 days
            print("\nNear Expiry Items:")
            for item in inv.near_expiry_items(7):
                print(item)
        elif choice == "7":
            # Exit the program
            print("Exiting...")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number from 1 to 7.")
