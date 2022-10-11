from abc import ABC, abstractmethod
class Bank(ABC):
   @abstractmethod
   def balance_check(self):
       pass
   @abstractmethod
   def interest(self):
       pass
class SBI(Bank):
   def balance_check(self):
       print("Balance is 100 rupees")
   def interest(self):
       print("SBI interest is 5 rupees")
       
class nekaDrugaBanka(Bank):
   def balance_check(self):
       print("Balance is 32000 euros")
   def interest(self):
       print("SBI interest is 3 euros")
       
       
s = SBI()
s.balance_check()
s.interest()