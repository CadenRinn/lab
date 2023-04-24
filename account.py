class Account:
  def __init__(self, name: str) -> None:
      """
      Constructor to create initial state of an account
      :param name: Name  of account holder
      """

      self.__account_name = name
      self.__account_balance = 0


  def deposit(self, amount: float) -> bool:

      """
      Method to deposit money into the account balance
      :param amount: Amount to be deposited to account_balance
      :return: Status of if money was deposited (True/False)
      """

      if amount>0:
          self.__account_balance += amount
          return True
      else:
          return False


  def withdraw(self, amount: float) -> bool:
      """
      Method to withdraw money from the account balance
      :param amount: Amount to be withdrawn from the account balance
      :return: Status of if money was withdrawn (True/False)
      """
      if amount <=0 or amount> self.__account_balance:
          return False
      else:
          self.__account_balance -= amount
          return True

  def get_balance(self) -> float:
      """
      Method that returns the account balance.
      :return: Account balance.
      """
      return self.__account_balance


  def get_name(self) -> str:
      """
      Method that returns the account name.
      :return: Account name
      """
      return self.__account_name
