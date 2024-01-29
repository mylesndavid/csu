#this assignment would not have be possible without using a dictionary for the items or a class. I did not see those requirements in the assignment description so I went with my discretion

#item class
class Item:
    def __init__(self, name, description = 'none', price = 0, quantity = 0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
    
    #returns the price name and quantity of the item
    def print(self):
        return f'{self.name} {self.quantity} @ {self.price} = {int(self.quantity) * int(self.price)}'

# shopping cart class 
class ShoppingCart():
    def __init__(self, name = 'none', date = 'January 1, 2020'):
        self.name = name
        self.date = date
        self.cart_items = []

    #adds given item to cart
    def add_item(self,itemToPurchase):
        self.cart_items.append(itemToPurchase)

    # removes given item from cart
    def remove_item(self, itemToRemove):
        for item in self.cart_items:
            if item.name == itemToRemove:
                self.cart_items.remove(item)
                return
        print(f'Item {itemToRemove} not found in the cart. Nothing removed')
    
    #modifies given item in cart if found and not previously modified
    def modify_item(self, itemToPurchase, newDesc, newPrice, newQuant): #itemToPurchase should be itemToModify but I am going with the instructions.
        item_found = False # because I need to use a class. I cannot simply use the "in" keyword and have to track if the item is found with a boolean
        for item in self.cart_items:
            if item.name == itemToPurchase:
                item_found = True
                if item.price == 0 and newPrice is not None:
                    item.price = newPrice
                else:
                    print(f'price already set for {item.name}')
                if item.description == 'none' and newDesc is not None:
                    item.description = newDesc
                else:
                    print(f'description already set for {item.name}')
                if item.quantity == 0 and newQuant is not None:
                    item.quantity = newQuant
                else:
                    print(f'quantity already set for {item.name}')
        if item_found == False:
            print(f'Item {itemToPurchase} not found in the cart. Nothing modified')

    #returns the number of items in the cart
    def get_num_items_in_cart(self):
        item_count = 0
        for item in self.cart_items:
            item_count += int(item.quantity)
        # print(f'{item_count} items in the cart')
        return(item_count)
    
    #gets cost of cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += int(item.price) * int(item.quantity)
        return f'total cost = ${total_cost}'
    
    #prints all items using print method in the item class and then the total of the cart
    def print_total(self):
        if len(self.cart_items) > 0:
            for item in self.cart_items:
                print(item.print())  # Call the print method of the Item class
            print(f'Total: ${self.get_cost_of_cart()}')
        else:
            print('SHOPPING CART IS EMPTY')

    #prints the descriptions of each item in cart
    def print_descriptions(self):
        for item in self.cart_items:
            print(f'item name: {item.name}. Item Description: {item.description}\n')

# print the menu and give options for choices
def print_menu(ShoppingCart: ShoppingCart):
    print(f"\n{ShoppingCart.name}'s Shopping Cart - {ShoppingCart.date}")
    choice = input("\nShopping Cart Menu\n"
                    "a - Add Item\n"
                    "r - Remove Item\n"
                    "c - Change Item\n"
                    "i - Output Item's Descriptions\n"
                    "o - Output shopping Cart\n"
                    "p - Shopping cart price\n"
                    "q - Quit\n"
                    "Choose an option: ")
    match choice:
        case 'a':
            print(f"Add Item\n{ShoppingCart.name}'s Shopping Cart - {ShoppingCart.date}")
            item = input('Item to add: ')
            new_item = Item(name=item)
            ShoppingCart.add_item(new_item)
        case 'r':
            print(f"Remove Item\n{ShoppingCart.name}'s Shopping Cart - {ShoppingCart.date}")
            item = input('Item to remove: ')
            ShoppingCart.remove_item(item)
        case 'c':
            print(f"Modify Item\n{ShoppingCart.name}'s Shopping Cart - {ShoppingCart.date}")
            print('(Leave field blank if you do not want to modify that attribute)\n')
            item = input('Item to modify: ')
            new_description = input('New description: ')
            new_price = input('New price: ')
            new_quantity = input('New quantity: ')
            ShoppingCart.modify_item(itemToPurchase=item, newDesc=new_description, newQuant=new_quantity, newPrice=new_price)
        case 'i':
            print(f"Item Descriptions\n{ShoppingCart.name}'s Shopping Cart - {ShoppingCart.date}")
            ShoppingCart.print_descriptions()
        case 'o':
            print(f"Output shopping cart\n{ShoppingCart.name}'s Shopping Cart - {ShoppingCart.date}")
            ShoppingCart.print_total()
        case 'q':
            exit()
        case _:
            print('Invalid Choice')



user_name = input('Enter your name: ')
shopping_date = input('enter the date ')
my_cart = ShoppingCart(name=user_name, date=shopping_date)

while True:
    print_menu(my_cart)
