import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
      "id": 1,
      "name": "Sydney Noh",
      "address": "966 Software School Rd.",
      "email": "sydneynoh@mail.com",
      "status": "Active"
    },
    {
      "id": 2,
      "name": "Trevor Guinn",
      "address": "123 NSS Ln",
      "email": "trevorguinn@mail.com",
      "status": "Active"
    },
    {
      "id": 3,
      "name": "Steven Nagel",
      "address": "345 Somewhere St",
      "email": "stevennagel@mail.com",
      "status": "Active"
    },
    {
      "id": 4,
      "name": "Ricky Bobby",
      "address": "678 IwantToGoFast Dr.",
      "email": "rickybobby@mail.com",
      "status": "Active"
    },
    {
      "name": "Customer 5",
      "address": "222 Place Dr",
      "id": 5,
      "email": "customer5@mail.com",
      "status": "Active"
    },
    {
      "name": "Customer 6",
      "address": "222 Road Pl",
      "id": 6,
      "email": "customer6@mail.com",
      "status": "Active"
    },
    {
      "email": "billybob@mail.com",
      "name": "Billy Bob",
      "id": 7,
      "address": "888 Road Pl",
      "status": "Active"
    }
]

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        # Initialize an empty list to hold all animal representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
      SELECT
          a.id,
          a.name,
          a.address,
          a.email,
          a.password
      FROM customer a
      WHERE a.id = ?
      """, (id,))
      
      data = db_cursor.fetchone()
      
      customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'])
      
      return json.dumps(customer.__dict__)
  
def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer
  
def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
            
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
        
def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break