class Account:
   def __init__(self, name: str) -> None:
       self.__account_name = name
       self.__account_balance = 0

   def deposit(self, amount: float) -> bool:
       if amount>0:
           self.__account_balance += amount
           return True
       else:
           return False

   def withdraw(self, amount: float) -> bool:
       if amount <=0 or amount> self.__account_balance:
           return False
       else:
           self.__account_balance -= amount
           return True


   def get_balance(self) -> float:
       return self.__account_balance


   def get_name(self) -> str:
       return self.__account_name