class Category:
  name = ""
  total = 0
  category_list = []
  amonut_d = 0
  withdrawals = 0
  percent = 0

  #constructor
  def __init__(self, name):
    self.category_list.append(name)
    self.name = name
    self.ledger = []
    return
  
  def deposit(self, amount, description = ""):
    self.total = self.total + amount
    self.amount_d = amount
    #dictionary for correct form of storing data
    thisdict = {
      "amount": amount,
      "description": description
    }
    self.ledger.append(thisdict)

  def withdraw(self, amount, description = ""):
    if(self.check_funds(amount)):
      self.withdrawals = self.withdrawals + amount
      self.total = self.total - amount #changing sign for print
      thisdict = {
      "amount": -amount,
      "description": description
      }
      self.ledger.append(thisdict)
      return True
    else:
      return False
  
  def get_balance(self):
    return(self.total)

  #transfer reusing withdraw and deposit
  def transfer(self, amount, name_t):
    if(self.withdraw(amount, "Transfer to " + name_t.name)):
      name_t.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    if(self.total >= amount):
      return True
    else:
      return False
  
  #printing
  def __str__(self):
    a_str = self.name.center(30, "*") + "\n"
    for i in range(len(self.ledger)):
      thisdict = self.ledger[i]
      des = thisdict["description"]
      amv = "{:.2f}"
      value = thisdict["amount"]
      
      if(len(des) > 23):
        a_str = a_str + des[:23] + amv.format(value).rjust(30 - 23) + "\n"
      else:
        a_str = a_str + des[:23] + amv.format(value).rjust(30 - len(des)) + "\n"
    
    
    
    a_str = a_str + "Total: " + str(self.total)
    return(a_str)
    
    

def create_spend_chart(categories):
  for category in categories:
    category.percent = category.withdrawals / 150 * 10
    category.percent = int(category.percent)
    category.percent = round(category.percent)
  
  c_str = "Percentage spent by category\n100|"
  i = 10
  while i > 0:
    for category in categories:
      if category.percent >= i:
        c_str = c_str + " o "
      else:
        c_str = c_str + "   "
    c_str = c_str + " "
    i = i - 1
    if(i != 0):
      c_str = c_str + "\n " + str(i) + "0|"

  c_str = c_str + "\n  0|"
  for category in categories:
    c_str = c_str + " o "
  c_str = c_str + " \n    "
  line = "-" * len(categories) * 3 + "-"
  c_str = c_str + line + "\n    "
  names = []
  for category in categories:
    names.append(len(category.name))
  longest = max(names)
  for i in range(longest):
    for category in categories:
      if i < len(category.name):
        c_str = c_str + " " + category.name[i] + " "
      else:
        c_str = c_str + "   "
    if i != longest - 1:
      c_str = c_str + " \n    " 
  c_str = c_str + " "
  return c_str
  