# database.py
# Handles all the methods interacting with the database of the application.
# Students must implement their own methods here to meet the project requirements.

import os
import pymysql.cursors

db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


def connect():
  try:
    conn = pymysql.connect(host=db_host,
                           port=3306,
                           user=db_username,
                           password=db_password,
                           db=db_name,
                           charset="utf8mb4",
                           cursorclass=pymysql.cursors.DictCursor)
    print("Bot connected to database {}".format(db_name))
    return conn
  except:
    print(
      "Bot failed to create a connection with your database because your secret environment variables "
      + "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
    print("\n")
# your code here
    #1st requirment 
def get_response(msg):
    db_response = None
    command_parts = msg.split()
    bot_command = command_parts[0]
    if "/find_account_information" in bot_command:
      db_response = Account_info()
    elif "/find_email_account" in bot_command:
      db_response = Account_email()
    elif "/find_customer_age" in bot_command:
      db_response = custAge()
    elif "/find_waiters_more_ten_customers" in bot_command:
      db_response = waiterTenCust()
    elif "/find_customer_can_drink" in bot_command:
      db_response = canDrink()
    elif "/find_elite_staff" in bot_command:
      db_response = eliteStaff()
    elif "/find_number_big_meals_on_menu" in bot_command:
      db_response = bigMeal()
    elif "/find_if_menu_is_updated" in bot_command:
      db_response = updateMenu()
    elif "/find_most_ordered_meal" in bot_command:
      db_response = mostOrdered()
    elif "/find_least_ordered_meal" in bot_command:
      db_response = leastOrdered()
    elif "/find_number_of_elite_cashiers" in bot_command:
      db_response = eliteCashiers()
    elif "/find_a_in_meals" in bot_command:
      db_response = aInMeals()
    elif "/find_e_in_staff" in bot_command:
      db_response = eInStaff()
    elif "/find_long_names_staff" in bot_command:
      db_response = staffLongName()
    elif "/find_number_loyal_customers" in bot_command:
      db_response = loyalCustomers()
    elif "/update_account_count_newHire" in bot_command:
      db_response = updateStaff()
    elif "/delete_staff_if_quit" in bot_command:
      db_response = getEmOut()
    else:
      return "Unkown command"
    return db_response

def Account_info():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT * FROM Account"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result
  
def Account_email():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT email FROM Account"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def custAge():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT name, age FROM Account WHERE age >= 21"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result
def waiterTenCust():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT COUNT(*) FROM Staff INNER JOIN Role ON Staff.staff_id = Role.role_id INNER JOIN Restaurant ON Staff.staff_id = Restaurant.staff_count WHERE Role.title = 'waiter' AND Restaurant.staff_count > 10;"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result
def canDrink():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT CASE WHEN age> 21 THEN 'CAN BE SERVER ALCOHOL'              ELSE 'CUSTOMERS AGE HAS TO BE 21 OR OLDER' END FROM                Account"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result
def eliteStaff():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT COUNT(*) FROM Staff WHERE years >= 3"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result
def bigMeal():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT COUNT(*) FROM Menu WHERE ingredients > 10"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result
  
def updateMenu():
  connection = connect()
  cursor = connection.cursor()
  query = "UPDATE Menu SET meal = 'new meal', ingredients = 20 WHERE menu_id = 1;"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result
  
def mostOrdered():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT meal FROM Menu JOIN ORDER ON Menu.menu_id = Order.menu_id GROUP BY meal ORDER BY COUNT(*) DESC LIMIT 1;"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def leastOrdered():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT meal FROM Menu JOIN ORDER ON Menu.menu_id = Order.menu_id GROUP BY meal ORDER BY COUNT(*) ASC LIMIT 1;"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def eliteCashiers():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT COUNT(*) FROM Staff INNER JOIN Role ON Staff.staff_id = Role.role_id INNER JOIN Payment ON Staff.staff_id = Payment.payment_id WHERE Role.title = 'cashier' AND Payment.payments > 100;"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def aInMeals():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT meal FROM Menu WHERE meal LIKE '%a%';"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def eInStaff():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT staff_id, name FROM Staff WHERE name LIKE '%e%';"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def staffLongName():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT staff_id, name FROM Staff WHERE LENGTH(name) >= 8;"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def loyalCustomers():
  connection = connect()
  cursor = connection.cursor()
  query = "SELECT COUNT(*) FROM Customer JOIN Order ON Customer.customer_id = Order.customer_id GROUP BY customer_id HAVING COUNT(*) > 5;"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def updateStaff():
  connection = connect()
  cursor = connection.cursor()
  query = "UPDATE Account SET account_id = account_id + 1 WHERE DOH >= CURDATE();"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result

def getEmOut():
  connection = connect()
  cursor = connection.cursor()
  query = "CREATE FUNCTION delete_account_if_staff_quit(staff_id INT) RETURNS INT BEGIN DECLARE quit_date DATE; SELECT quit_date INTO quit_date FROM Staff WHERE staff_id = staff_id; IF quit_date IS NOT NULL THEN DELETE FROM Account WHERE staff_id = staff_id; RETURN 1; ELSE RETURN 0; END IF; END;"
  cursor.execute(query)
  query_result = cursor.fetchall()
  cursor.close()
  return query_result