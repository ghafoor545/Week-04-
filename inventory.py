import datetime  # Importing datetime module for date operations
import csv  # Importing csv module for CSV file operations
from .fooditems import FoodItem  # Importing FoodItem class from fooditems module

class Inventory:
    def __init__(self, filename='inventory.csv'):
        """
        Initialize Inventory object.

        Args:
            filename (str): Optional. Filename of the CSV inventory file. Default is 'inventory.csv'.
        """
        self.food_items = []  # Initialize an empty list to store food items
        self.filename = filename  # Store the filename for the inventory CSV file
        self.load_inventory()  # Load inventory data from the CSV file upon initialization

    def load_inventory(self):
        """
        Load inventory data from CSV file into self.food_items list.
        Handles exceptions like FileNotFoundError and general Exception during loading.
        """
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)  # Create a CSV reader object
                for row in reader:
                    name, category, quantity, barcode, expiry_date = row
                    # Create a FoodItem object and append to self.food_items list
                    food_item = FoodItem(name, category, int(quantity), barcode, datetime.datetime.strptime(expiry_date, '%Y-%m-%d').date())
                    self.food_items.append(food_item)
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty inventory.")
        except Exception as e:
            print(f"Error loading inventory: {e}")

    def save_inventory(self):
        """
        Save inventory data from self.food_items list to CSV file.
        Handles exceptions during saving.
        """
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)  # Create a CSV writer object
                for item in self.food_items:
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date])
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_food_item(self, food_item):
        """
        Add a FoodItem object to self.food_items list and save to CSV file.
        
        Args:
            food_item (FoodItem): FoodItem object to add.
        """
        self.food_items.append(food_item)  # Append food_item to the list
        self.save_inventory()  # Save updated inventory to CSV file
        print(f"Added: {food_item}")

    def edit_food_item(self, barcode, name=None, category=None, quantity=None, expiry_date=None):
        """
        Edit attributes of a FoodItem object based on barcode.
        Save updated inventory to CSV file.
        
        Args:
            barcode (str): Barcode of the FoodItem to edit.
            name (str): Optional. New name for the FoodItem.
            category (str): Optional. New category for the FoodItem.
            quantity (int): Optional. New quantity for the FoodItem.
            expiry_date (str or datetime.date): Optional. New expiry date for the FoodItem.
        """
        for item in self.food_items:
            if item.barcode == barcode:  # Find the FoodItem by barcode
                if name:
                    item.name = name  # Update name if provided
                if category:
                    item.category = category  # Update category if provided
                if quantity is not None:
                    item.quantity = quantity  # Update quantity if provided
                if expiry_date:
                    item.expiry_date = expiry_date  # Update expiry_date if provided
                self.save_inventory()  # Save updated inventory to CSV file
                print(f"Edited: {item}")
                return True
        print("Edit failed: Item not found.")
        return False

    def delete_food_item(self, barcode):
        """
        Delete a FoodItem object from self.food_items list based on barcode.
        Save updated inventory to CSV file.
        
        Args:
            barcode (str): Barcode of the FoodItem to delete.
        """
        for item in self.food_items:
            if item.barcode == barcode:  # Find the FoodItem by barcode
                self.food_items.remove(item)  # Remove the FoodItem from the list
                self.save_inventory()  # Save updated inventory to CSV file
                print(f"Deleted: {item}")
                return True
        print("Delete failed: Item not found.")
        return False

    def search_food_item(self, barcode):
        """
        Search for a FoodItem object in self.food_items list based on barcode.
        
        Args:
            barcode (str): Barcode of the FoodItem to search for.
        
        Returns:
            FoodItem or None: Returns the FoodItem object if found, otherwise returns None.
        """
        for item in self.food_items:
            if item.barcode == barcode:  # Find the FoodItem by barcode
                return item
        return None  # Return None if FoodItem is not found

    def near_expiry_items(self, days=7):
        """
        Retrieve a list of FoodItem objects that are near expiry within a specified number of days.
        
        Args:
            days (int): Number of days within which the expiry date falls to consider as near expiry.
        
        Returns:
            list: List of FoodItem objects that are near expiry.
        """
        near_expiry = []
        today = datetime.date.today()  # Get today's date
        for item in self.food_items:
            if (item.expiry_date - today).days <= days:  # Calculate days until expiry
                near_expiry.append(item)  # Add item to near_expiry list
        return near_expiry  # Return list of near expiry FoodItem objects

    def display_inventory(self):
        """
        Display all FoodItem objects in self.food_items list.
        """
        print("\nCurrent Inventory:")
        for item in self.food_items:
            print(item)  # Print string representation of each FoodItem object
