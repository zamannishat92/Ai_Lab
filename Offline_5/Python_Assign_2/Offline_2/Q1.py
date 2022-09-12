#Create two instances of Bank class, b1=Bank(“DBBL”, 1256) and b2=(“EBL”, 1257). Initialize the branch_list as an empty list for both of the banks.
    
class Bank:
  def __init__(self,name,code):
    self.name=name
    self.code=code
    self.branch_list=[]

  def addBranch(self,branch_obj):
    self.branch_list.append(branch_obj)

  def removeBranch(self,branch_code):
    for branch_obj in branch_list:
      if branch_obj.code == branch_code:
        branch_list.remove(branch_obj)

  def getBranch(self,branch_code):
    for branch_obj in branch_list:
      if branch_obj.code == branch_code:
        return branch_obj
      else:
        return None

  def getAllBranches(self):
    for branch_obj in branch_list:
      print(branch_obj.code)
      print(branch_obj.city)

   
class Branch:
  def __init__(self,branch_code,city,bank):
    self.branch_code = branch_code
    self.city = city
    self.bank = bank
    self.account_list = []

  def addAccount(self,account_obj):
    self.account_list.append(account_obj)

  def removeAccount(self,account_number):
    for acc in account_list:
      account_list.remove(acc)

  def getAccount(self,account_number):
     for acc in account_list:
       if acc.num==account_number:
         return acc
       else:
         return None
  #def updateInfo(self,branch_code,city):



class Account:
  def __init__(self,acc_no,branch_obj):
    self.acc_no=acc_no
    self.branch_obj=branch_obj
    self.balance=0
  
  def debitAmount(self,amt):
    self.balance-=amt

  def creditAmount(self,amt):
    self.balance+=amt

  def getBalance(self):
    return self.balance

class Savings_Account(Account):
  def __init__(self,acc_no,branch,min_balance):
    super().__init__(acc_no,branch)
    self.min_balance=min_balance
    self.open_date=datetime.datetime.now()
    self.customer=None
  
  def setCustomer(self,customer_obj):
    self.customer=customer_obj

  def removeCustomer(self):
    self.customer=None
  
class Current_Account(Account):
  def __init__(self,acc_no,branch,interest_rate):
    super().__init__(acc_no,branch)
    self.interest_rate=interest_rate
    self.open_date=datetime.datetime.now()
    self.customer=None

  def setCustomer(self,customer_obj):
    self.customer=customer_obj

  def removeCustomer(self):
    self.customer=None

class Customer:
  next_id=1
  def __init__(self,name,address,phone):
    self.name=name
    self.address=address
    self.phone=phone
    self.saving_acc=None
    self.current_acc=None
    self.id=id

    Customer.next_id+=1
    Customer.next_id=self.id
  
  def setSavingsAcc(self,savings_acc):
    self.saving_acc=savings_acc

  def getSavingsAcc(self):
    return self.saving_acc

  def setCurrentAcc(self,current_acc):
    self.current_acc=current_acc

  def getCurrentAcc(self):
    return self.current_acc 
    

  b1=Bank("DBBL", 1256)
  b2=Bank("EBL", 1257)

  br1=Branch(1,'Dhanmondi',b1)
  br2=Branch(2, 'Motijheel',b1)
  br3=Branch(3, 'Motijheel',b2)
  br4=Branch(4,'Gulshan',b2)

  b1.addBranch(br1)
  b1.addBranch(br2)
  b2.addBranch(br3)
  b2.addBranch(br4)

  cs1=Customer("Afif", "Dhaka", "01911111111")
  cs2=Customer("Sohan","Dhaka","01511111111")

  
  
  

  


