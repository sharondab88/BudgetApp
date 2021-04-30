#global amount
#global balance
#helps keep running total(s)

import time
localtime = time.asctime(time.localtime(time.time()))
print("Current local time is :", localtime)

class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "You've deposited ${} in the {} budget.".format(amount, self.category)

    def withdraw(self, amount):
        if self.amount <= amount:
             return "You dont have enough funds in your {} budget to withdraw ${}!".format(self.category, amount)
        else:
            self.amount -= amount
            return "You withdrew ${} from {} budget.".format(amount, self.category)
            pass

    def budget_balance(self):
        return "Your current balance is: ${}" .format(self.amount)

    def check_balance(self, amount):
        return;
        #update per feedback

    def transfer(self, category, amount):
        self.amount -= amount
        category.amount += amount
        #made update per feedback

food_category = Budget("Food", 1000)
clothing_category = Budget("Clothing", 1000)
car_category = Budget("Car", 1000)

# Adding money to balances
print(food_category.deposit(1000))
print(clothing_category.deposit(1000))

# Checking balances
print(food_category.check_balance(food_category))
print(clothing_category.check_balance(clothing_category))
print(car_category.check_balance(car_category))

# making withdrawals
print(food_category.withdraw(1500))
print(clothing_category.withdraw(250))
print(car_category.withdraw(1100))



