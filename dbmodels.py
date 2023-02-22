from sqlalchemy
import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative
import declarative_base

Base = declarative_base()

class Account(Base):
  tablename = 'Account'

  account_id = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  DOH = Column(String(45), nullable=False)
  state = Column(String(45), nullable=False)
  age = Column(Integer, nullable=False)

  def init(self, account_id, name, DOH, state, city):
    self.account_id = account_id
    self.name = name
    self.DOH = DOH
    self.state = city
   

class Staff(Base):
  tablename = 'Staff'

  staff_id = Column(Integer, primary_key=True)
  role = Column(String(45), nullable=False)
  account = Column(String(45), nullable=False)
  years = Column(Integer, nullable=False)
  
  def init(self, staff_id, role, account, years):
    self.staff_id = staff_id
    self.role = role
    self.account = account
    self.years = years
    
class Restaurnat (Base):
  tablename = 'Restaurnat'

  restaurant_id = Column(Integer, primary_key=True)
  location = Column(String(45), nullable=False)
  phone = Column(long, nullable=False)
  staff_count = Column(Integer, nullable=False)
  
  def init(self, restaurant_id, location, phone, staff_count):
    self.restaurant_id = restaurant_id
    self.location = location
    self.phone = phone
    self.staff_count = staff_count
    
class Role (Base):
  tablename = 'Role'

  role_id = Column(Integer, primary_key=True)
  title = Column(String(45), nullable=False)
  
  def init(self, role_id, title):
    self.role_id = role_id
    self.title = title
   
class Menu (Base):
  tablename = 'Menu'

  menu_id = Column(Integer, primary_key=True)
  meal = Column(String(45), nullable=False)

  def init(self, menu_id, meal, phone, staff_count):
    self.menu_id = menu_id
    self.meal = meal

class Payment (Base):
  tablename = 'Payment'

  payment_id = Column(Integer, primary_key=True)
  amount = Column(double, nullable=False)
  date = Column(date, nullable=False)
  
  def init(self, payment_id, amount, date):
    self.payment_id = payment_id
    self.amount = amount
    self.date = date

class Customer(Base):
  tablename = 'Staff'

  customer_id = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  age = Column(String(45), nullable=False)
  
  def init(self, customer_id, name, age):
    self.customer_id = customer_id
    self.name = name
    self.age = age

class Waiter(Base):
  tablename = 'Waiter'

  waiter_id = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  age = Column(Integer, nullable=False)
  serve = Column(Integer, nullable=False)
  
  def init(self, waiter_id, name, age, serve):
    self.waiter_id = waiter_id
    self.name = name
    self.age = age    
    self.server = serve
    
class Manager(Base):
  tablename = 'Manager'

  manager_id = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  age = Column(Integer, nullable=False)
  edits_menu = Column(Integer, nullable=False)
  
  def init(self, manager_id, name, age, edits_menu):
    self.manager_id = manager_id
    self.name = name
    self.age = age    
    self.edits_menu = edits_menu

class Manager(Base):
  tablename = 'Manager'

  manager_id = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  age = Column(Integer, nullable=False)
  edits_menu = Column(Integer, nullable=False)
  
  def init(self, manager_id, name, age, edits_menu):
    self.manager_id = manager_id
    self.name = name
    self.age = age    
    self.edits_menu = edits_menu

class Supplier(Base):
  tablename = 'Supplier'

  supplier_id = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  age = Column(Integer, nullable=False)
  
  def init(self, supplier_id, name, age):
    self.supplier_id = supplier_id
    self.name = name
    self.age = age    

class Cashier(Base):
  tablename = 'Cashier'

  cashier_id = Column(Integer, primary_key=True)
  name = Column(String(45), nullable=False)
  age = Column(Integer, nullable=False)
  process = Column(Integer, nullable=False)
  
  def init(self, cashier_id, name, age, process):
    self.cashier_id = cashier_id
    self.name = name
    self.age = age    
    self.process = process
    
class Meal(Base):
  tablename = 'Meal'

  meal_id = Column(Integer, primary_key=True)
  price = Column(Integer, nullable=False)
  name = Column(String(45), nullable=False)
  ingredient = Column(Integer, nullable=False)
  
  def init(self, meal_id, price, name, ingredient):
    self.meal_id = meal_id
    self.price = price
    self.name = name    
    self.ingredient = ingredient