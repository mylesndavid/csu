#ItemToPurchase Class
class ItemToPurchase():
    def __init__(self, name ='none', price=float(0), quantity = int(0)):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        cost = float(self.item_price) * int(self.item_quantity)
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = {cost}')
        return cost

#prompt user for items and instantiate ItemToPurchase Objects
print('Item 1')
i1name = input('Enter the Item Name: ')
i1price = input('Enter the Item Price: ')
i1quantity = input('Enter the item Quantity: ')

item1 = ItemToPurchase(i1name,i1price,i1quantity)

print('\nItem 2')
i2name = input('Enter the Item Name: ')
i2price = input('Enter the Item Price: ')
i2quantity = input('Enter the item Quantity: ')

item2 = ItemToPurchase(i2name,i2price,i2quantity)

#print total cost
print(f'\nTotal: ${item1.print_item_cost() + item2.print_item_cost():.2f}')
