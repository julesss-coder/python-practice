# Following along to tutorial "Object Oriented Programming with Python - Full Course for Beginners", URL: https://www.youtube.com/watch?v=Ej_02ICOIgs&t=4402s
# Continue at mark 38:30
class Item:
  # Class attributes - attributes that apply to all instances. Can be accessed from class AND instances. Instances look in their instance attributes first before looking for class attributes of the same name. 
  pay_rate = 0.8


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

  # When you call this method, Python passes the instance of the class to the method as the first argument. So, ALL methods must at least have the parameter `self`
  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    return self.price * Item.pay_rate


item1 = Item("phone", 1, 3)
item2 = Item("laptop", 300, 2)
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price())
print("Item.pay_rate: ", Item.pay_rate)
print("item1.pay_rate: ", item1.pay_rate)
# Access all class attributes of this class, converted to a dictionary
print("Item.__dict__: ", Item.__dict__)
# Access all instance attributes of this instance, converted to a dictionary
print("item1.__dict__: ", item1.__dict__)

