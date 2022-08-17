class inventory():
    def __init__(self,item,stock, date,price):
        self.items = item
        self.stock = stock
        self.date = date
        self.price= price
    
inventory1=inventory('bread',20,'Sep 2022',70)
inventory2=inventory('sugar', 15, 2023, 170)
print(inventory1)
