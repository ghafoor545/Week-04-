import datetime  # Import the datetime module for handling dates

class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        """
        Initialize a FoodItem object with provided attributes.

        Args:
            name (str): Name of the food item.
            category (str): Category of the food item.
            quantity (int): Quantity of the food item.
            barcode (str): Barcode of the food item.
            expiry_date (str or datetime.date): Expiry date of the food item.
                If str, it will be converted to datetime.date using '%Y-%m-%d' format.
        """
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = self._parse_expiry_date(expiry_date)

    def _parse_expiry_date(self, expiry_date):
        """
        Parse expiry date into a datetime.date object.

        Args:
            expiry_date (str or datetime.date): Expiry date to parse.

        Returns:
            datetime.date: Parsed expiry date as datetime.date object.
        """
        if isinstance(expiry_date, datetime.date):
            return expiry_date
        elif isinstance(expiry_date, str):
            return datetime.datetime.strptime(expiry_date, '%Y-%m-%d').date()
        else:
            raise ValueError("Invalid expiry date format. Expected str or datetime.date.")

    def __str__(self):
        """
        Return a string representation of the FoodItem object.

        Returns:
            str: String representation containing key attributes of the food item.
        """
        return f"Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Barcode: {self.barcode}, Expiry Date: {self.expiry_date}"
