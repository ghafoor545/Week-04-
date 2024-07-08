import datetime
import csv
from .fooditems import FoodItem

class Inventory:
    def __init__(self, filename='inventory.csv'):
        self.food_items = []
        self.filename = filename  # Store the filename as an attribute
        self.load_inventory()    # Load inventory data from the file on initialization

    def load_inventory(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, category, quantity, barcode, expiry_date = row
                    food_item = FoodItem(name, category, int(quantity), barcode, datetime.datetime.strptime(expiry_date, '%Y-%m-%d').date())
                    self.food_items.append(food_item)
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty inventory.")
        except Exception as e:
            print(f"Error loading inventory: {e}")

    def save_inventory(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                for item in self.food_items:
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date])
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_food_item(self, food_item):
        self.food_items.append(food_item)
        self.save_inventory()
        print(f"Added: {food_item}")

    def edit_food_item(self, barcode, name=None, category=None, quantity=None, expiry_date=None):
        for item in self.food_items:
            if item.barcode == barcode:
                if name:
                    item.name = name
                if category:
                    item.category = category
                if quantity is not None:
                    item.quantity = quantity
                if expiry_date:
                    item.expiry_date = expiry_date
                self.save_inventory()
                print(f"Edited: {item}")
                return True
        print("Edit failed: Item not found.")
        return False

    def delete_food_item(self, barcode):
        for item in self.food_items:
            if item.barcode == barcode:
                self.food_items.remove(item)
                self.save_inventory()
                print(f"Deleted: {item}")
                return True
        print("Delete failed: Item not found.")
        return False

    def search_food_item(self, barcode):
        for item in self.food_items:
            if item.barcode == barcode:
                return item
        return None

    def near_expiry_items(self, days=7):
        near_expiry = []
        today = datetime.date.today()
        for item in self.food_items:
            if (item.expiry_date - today).days <= days:
                near_expiry.append(item)
        return near_expiry

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for item in self.food_items:
            print(item)

# Example usage:
if __name__ == "__main__":
    inventory_file_path = "/Users/cv/Downloads/Task 04/inventory.csv"
    inventory = Inventory(filename=inventory_file_path)
    inventory.display_inventory()
