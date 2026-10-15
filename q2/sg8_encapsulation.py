class BankAccount: #Creates a class named "BankAccount", this serves as a blueprint for creating bank accounts
  def __init__(self, account_number, balance): # "__init__" is the constructor, it'll run automatically whenever i create a new back account. It'll also receive the acc. no. and initial balance
      self.__account_number = account_number # This stores the acc. number in a private attribute, so that it cannot be directly accesed outside the class
      self.__balance = 0 # Sets the balance to zero, before checing the balance that was given
      self.balance = balance # Assigns the initial balance using setter, and checks if ammount is valid before saving it

  def set_account_number(self, account_number): # Creates a method that allows me to change the acc. number 
      self.__account_number = account_number #Replaces old acc. number with new one

  @property
  def balance(self):
      return self.__balance

  @balance.setter
  def balance(self, amount):
      if amount >= 0:
          self.__balance = amount
      else:
          print("Warning: Balance cannot be negative!")

  @property
  def account_number(self):
      return self.__account_number

  @property
  def balance(self):
      return self.__balance

  @balance.setter
  def balance(self, amount):
      if amount >= 0:
          self.__balance = amount
      else:
          print("Warning: Balance cannot be negative!")

account = BankAccount("223201217232", 5000)
print("Account Number:", account.account_number)
print(f"Balance: P{account.balance:,.2f}")

account.set_account_number("962407621")
account.balance = 2167

print("\nUpdated Account Information")
print("Account Number:", account.account_number)
print(f"Balance: P{account.balance:,.2f}")

account.balance = -8090

print(f"Balance: P{account.balance:,.2f}")
