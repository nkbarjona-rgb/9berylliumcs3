class BankAccount:
  def __init__(self, account_number, balance):
      self.__account_number = account_number
      self.__balance = 0
      self.balance = balance

  def set_account_number(self, account_number):
      self.__account_number = account_number

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
