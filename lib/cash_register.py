#!/usr/bin/env python3
class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
# this will clear pytest 1- CashRegister in cash_register.py takes one optional argument, a discount, on initialization. 

    self.total = 0
  # this clears number 2- CashRegister in cash_register.py sets an instance variable total on initialization to zero. .  
    self.last_transaction = 0
    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.last_transaction = price * quantity
    self.total += self.last_transaction
# this will get numbers 3-5 passing:
# CashRegister in cash_register.py accepts a title and a price and increases the total. .                                             [ 23%]
# CashRegister in cash_register.py also accepts an optional quantity. .                                                               [ 30%]

    for _ in range(quantity):
      self.items.append(title)
# this will get numbers 6
# CashRegister in cash_register.py doesn"t forget about the previous total .

  def apply_discount(self):
    if (self.discount > 0):
      discount_as_percent = (100 - float(self.discount)) / 100
      self.total = int(self.total * discount_as_percent)

# this will clear number 8- CashRegister in cash_register.py applies the discount to the total price. .
      print(f"After the discount, the total comes to ${self.total}.")

#this clears 9-10
# CashRegister in cash_register.py prints success message with updated total .                                                        [ 53%]
#CashRegister in cash_register.py reduces the total . 
#  
    else:
      print('There is no discount to apply.')

#this clears 11-CashRegister in cash_register.py returns an array containing all items that have been added, including multiples .    

  def void_last_transaction(self):
    self.total -= self.last_transaction
    
# this clears final two:
# CashRegister in cash_register.py subtracts the last item from the total F                                                           [ 92%]
# CashRegister in cash_register.py returns the total to 0.0 if all items have been removed F