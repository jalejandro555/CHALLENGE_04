class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def calculate_total_price(self, quantity):
        return self.get_price() * quantity

class FoodItem(MenuItem):
    def __init__(self, name, price, category):
        super().__init__(name, price)
        self._category = category

    def get_category(self):
        return self._category

    def set_category(self, value):
        self._category = value

class Starters(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Starters")

class Soupes(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Soupes")

class MainCourse(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Main Course")

class Drinks(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Drinks")

class Dessert(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Dessert")

class Payment:
    def __init__(self):
        pass

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")

class Card(Payment):
    def __init__(self, number, cvv):
        super().__init__()
        self.number = number
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paying {amount} with card {self.number[-4:]}")

class Cash(Payment):
    def __init__(self, amount_given):
        super().__init__()
        self.amount_given = amount_given

    def pay(self, amount):
        if self.amount_given >= amount:
            print(f"Payment made in cash. Change: {self.amount_given - amount}")
        else:
            print(f"Insufficient funds. Missing {amount - self.amount_given} to complete the payment.")

def user_payment(total_after_discount):
    while True:
        print("Please select a payment method:")
        print("1. Card")
        print("2. Cash")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            card_number = input("Enter your card number: ")
            cvv = input("Enter your CVV: ")
            return Card(card_number, cvv)
        elif choice == '2':
            amount_given = float(input("Enter the amount you are giving: "))
            if amount_given < total_after_discount:
                print(f"Not enough money given. You still owe: ${total_after_discount - amount_given:.2f}")
            else:
                change = amount_given - total_after_discount
                print(f"Payment made in cash. Change: ${change:.2f}")
                return Cash(amount_given)
        else:
            print("Invalid choice. Please enter 1 or 2.")


# Define thezOrder class
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def calculate_total_price(self):
        total = 0
        for item, quantity in self.items:
            total += item.get_price() * quantity
        return total
    
    def ask_for_discount(self):
        categories = ["programmer", "mentally_ill", "student", "senior_citizen", "veteran", "unemployed", "homeless", "refugee", "disabled"]
        print("Please enter your population category. if you are not in any of these categories, please press enter")
        print("Available categories are:")
        for category in categories:
            print(category)
        user_category = input()
        if user_category in categories:
            return 10
        else:
            print("Sorry, you are not eligible for a discount.")
            return 0


    def apply_discount(self):
        discount = self.ask_for_discount()
        total_bill = self.calculate_total_price()
        return total_bill - (total_bill * discount / 100)

# Create instances of menu items
menu_items = [
    Starters("Diazepam, ONLY_FOR_SALE_WITH_PRESCRIPTION", 1.99,),
    Starters("Xanax, ONLY_FOR_SALE_WITH_PRESCRIPTION", 0.99),
    Starters("Propanonol, ONLY_FOR_SALE_WITH_PRESCRIPTION", 0.99), 
    Soupes("Programmer's tears with Mexican tortilla", 5.99),
    Soupes("Spinach with tomato", 3.99),
    Soupes("Lentil with bacon", 4.99),
    MainCourse("Korean boy beef burger", 201.99),
    MainCourse("Chicken fetus crepe", 122.99),
    MainCourse("Vegan salad with tuna", 7.99),
    MainCourse("Turkey pizza", 100),
    MainCourse("Venezuelan Pasta", 0.99),
    MainCourse("Fish and Chips with cornflakes", 12.99),
    Drinks("Fanta", 1.99),
    Drinks("Taylor Swift's sweat", 900.99),
    Drinks("Coca Cola", 1.99),
    Drinks("Pepsi", 1.99),
    Drinks("Water from arctic glaciers", 300.99),
    Dessert("Ice cream with an american sausage", 2.99),
    Dessert("Fruit salad without fruit or transgenic fruit", 2.99),
    Dessert("Fruit salad with organic fruit", 200.99),
    Dessert("Snow white apple, REQUIRES_SIGNED_CONSENT", 6.99),
]
# User interaction functions
def show_menu():
    print("Menu:")
    for index, item in enumerate(menu_items):
        print(f"{index + 1}. {item.get_name()} - ${item.get_price()} - Category: {item.get_category()}")
def user_order():
    show_menu()
    order = Order()
    while True:
        choice = input("Enter the menu item number (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        order.add_item(menu_items[int(choice) - 1], quantity)
    return order

# Main program
if __name__ == "__main__":
    print("WELCOME TO THE PYTHON PSYCHIATRIC RESTAURANT!")
    customer_order = user_order()
    print(f"Your total bill is: ${customer_order.calculate_total_price():.2f}")
    total_after_discount = customer_order.apply_discount()
    print(f"Your total bill after discount is: ${total_after_discount:.2f}")
    payment_method = user_payment(total_after_discount)
   
    print("Thank you for dining with us!")

    