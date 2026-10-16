class BankAccount: #Creates a class named "BankAccount", this serves as a blueprint for creating bank accounts
  def __init__(self, account_number, balance): # "__init__" acts as the constructor, it will run automatically whenever i create a new back account. It'll also receive the account number and initial balance
      self.__account_number = account_number # Stores account number as a private attribute, so that it cant be accesed directly outside the class
      self.__balance = 0 # Sets balance to zero, before checking the balance that was given
      self.balance = balance # Assigns initial balance using the setter, and checks if the ammount is valid before saving it

  def set_account_number(self, account_number): # Creates a method that lets me change the account number 
      self.__account_number = account_number # Replaces old account number with new one

  @property # allows me to acces the balance like a normal attribute, instead of calling it a method
  def balance(self): # same as text above 
      return self.__balance # returns current balance, so It can be displayed or used

  @balance.setter # controls what happens when I'll try to change the balance, the new value is stored in the varaible "amount"
  def balance(self, amount): # same as text above
      if amount >= 0: # checks if amount is zero or positive
          self.__balance = amount # if "amount" is valid, it saves it as its new balance
      else: # if not, it goes to the code below
          print("Warning: Balance cannot be negative!") # shows a warning when i try to set a negative balance, whilst the existing balance stays the same

  @property # allows me to access the account number like a attribute
  def account_number(self): # same as text above
      return self.__account_number # returns stored account number so i can use or display it

  @property # allows me to access the balance like a normal attribute
  def balance(self): # same as text above
      return self.__balance # returns stored balance so i can use or display it

  @balance.setter # lets me control what happens when i try to change the balance
  def balance(self, amount): #defines the setter.self which refers to the account, whilst amount is the new balance ill try to set
      if amount >= 0: # checks if new balance is zero or positive
          self.__balance = amount # if amount or new balance is valid, it saves as the accounts new balance
      else: # if amount is negative, code goes to here
          print("Warning: Balance cannot be negative!") # displays a warning without changing existing balance

account = BankAccount("223201217232", 5000) # creates a bank account with account number "223201217232" and an intial balance of 5k pesos
print("Account Number:", account.account_number) # dispalys account number by accessing its property
print(f"Balance: P{account.balance:,.2f}") # displays balance in pesos, "f" lets me insert value into the text, whilst ",.2f" formats number properly

account.set_account_number("962407621") # changes account number to "962407621," this is through the method i made earlier on in the code 
account.balance = 2167 # changes the balance to 2167 pesos, setter will check ammount, and accept as its not negative

print("\nUpdated Account Information") # displays heading to update that the info has been updated, whilst "\n" adds a blank line before the heading
print("Account Number:", account.account_number) # displays new/updated account number
print(f"Balance: P{account.balance:,.2f}") # displays new/updated balance

account.balance = -8090 # tries to change balance to a negative amount, "setter" checks it and rejects the change because negative balance is not allowed

print(f"Balance: P{account.balance:,.2f}") # formats and displays current balance, since the negative amount was not accepted
