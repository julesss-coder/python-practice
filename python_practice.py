# 7.8., 8:30 - 10:00
# Following along to tutorial "Object Oriented Programming with Python - Full Course for Beginners", URL: https://www.youtube.com/watch?v=Ej_02ICOIgs&t=4402s
# Continue at mark 1:04:00

# =====================================

import csv

class Item:
  # Class attributes - attributes that apply to all instances. Can be accessed from class AND instances. Instances look in their instance attributes first before looking for class attributes of the same name. 
  pay_rate = 0.8
  all = []


  # When you instantiate a class, Python call __init__() method automatically
  # Use a default parameter if you don't always have objects of this type
  # Specify a data type for each parameter. (Passing in a default value signifies that the given data type is expected.)
  def __init__(self, name: str, price: float, quantity=0):
    # Validate arguments received. Add assertion error messages.
    assert price >= 0, f"Price {price} is not greater than 0!"
    assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"

    # Assign arguments to self object
    self.name = name
    self.price = price
    self.quantity = quantity

    # Actions to execute
    Item.all.append(self)

  # When you call this method, Python passes the instance of the class to the method as the first argument. So, ALL methods must at least have the parameter `self`
  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    # was ist pay_rate, wenn ich es als Instanz- und Klassenfeld habe?
    # Erwartung: Der Wert des Instanzfeldes
    # Realität: 100%
    self.price = self.price * self.pay_rate

  # Represent the instance in a human-readable way
  def __repr__(self):
    # Represent the instance the way you created it
    return f"Item('{self.name}', {self.price}, {self.quantity})"

  # A class method does not have the `self` parameter, as it is attached to the class. Instead, it uses the `cls` (for 'class') parameter
  @classmethod
  def instantiate_from_csv(cls):
    with open('python-practice/items.csv', 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      items = list(reader)

    for item in items:
        Item(
          name=item.get('name'),
          price=float(item.get('price')),
          quantity=int(item.get('quantity'))
        )


Item.instantiate_from_csv()

print(Item.all)
for item in Item.all:
    # Prints item the way it is represented in item.__repr__
    print(item)
