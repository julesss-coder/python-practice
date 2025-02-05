# 7.8., 8:30 - 10:00
# 22.1.2025, 8:34 - 9:04, mark 23:54
# 22.1.2025, 18:02 - 18:52, mark 47:40
# 29.1.2025, 8:00 - 9:00, mark 59:39 
# 29.1.2025, 16:34 - 17:52 - mark 1:21:13
# 5.2.2025, 8:50-9:37, mark 1:28:45
# 5.2.2025, 17:48 - , mark 1:51:03
# Following along to tutorial "Object Oriented Programming with Python - Full Course for Beginners", URL: https://www.youtube.com/watch?v=Ej_02ICOIgs&t=4402s
# Continue at mark 1:14:00

# =====================================

import csv

class Item:
  # Class attributes - attributes that apply to all instances. Can be accessed from class AND instances. Instances look in their instance attributes first before looking for class attributes of the same name. 
  pay_rate = 0.8
  all = []

  # When you instantiate a class, Python calls __init__() method automatically
  # Use a default parameter if you don't always have objects of this type
  # Specify a data type for each parameter. (Passing in a default value signifies that the given data type is expected.)
  # BUT type is just for documentation, does not force error
  def __init__(self, name: str, price: float, quantity: int): # TODO Warum bekomme ich KEINE Fehlermeldung, wenn ich eine Float übergebe?
    # Validate arguments received. Add assertion error messages.
    assert price >= 0, f"Price {price} is not greater than 0!"
    assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"

    # Assign arguments to self object
    self.__name = name
    self.price = price
    self.quantity = quantity

    # Actions to execute
    Item.all.append(self)


  @property
  def name(self):
    return self.__name.upper()

  @name.setter
  def set_name(self, name):
      self.__name = name

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
    return f"Item:'{self.name}', {self.price}, {self.quantity}"

  # A class method does not have the `self` parameter, as it is attached to the class. Instead, it uses the `cls` (for 'class') parameter
  @classmethod
  def instantiate_from_csv(cls):
    with open('./items.csv', 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      items = list(reader)

    for item in items:
        Item(
          name=item.get('name'),
          price=float(item.get('price')),
          quantity=int(item.get('quantity'))
        )

  @staticmethod
  def is_integer(num):
    if isinstance(num, float):
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else:
      return False


# Item.instantiate_from_csv()

# print(Item.all)
# for item in Item.all:
#     # Prints item the way it is represented in item.__repr__
#     print(item)

# print(Item.is_integer('a'))
# print(Item('laptop', 10, 10).is_integer('a'))
# print(Item(3, 22.2, 3.3))
# print(Item.all)
phone = Item('phone', 20, 5)
# print(phone.__name) #erw.: error
phone.set_name = 'new name' 
print(phone.name) #erw 'new name'



class Person:
  sex = 'female'

  def __init__(self):
    self.name = "Julia"

julia = Person()
# print(julia.name) #exp: Julia, reality 100%
# print(Person.name) #exp: error => reality: AttributeError: type object 'Person' has no attribute 'name'
# print(julia.__dict__) #Exp. prints instance attributes, i.e. name; reality: {'name': 'Julia'}
# print(Person.__dict__) #Exp. prints class attributes, i.e. sex; reality: {'__module__': '__main__', 'sex': 'female', '__init__': <function Person.__init__ at 0x78d0728a6520>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


# print(dir(Item))

class Phone(Item):
  pass

# print(Phone('test item', 20, 1))

# print(Phone.__class__)
# print(Phone.__class__.__name__)


