CUSTOMERS = [
    {
      "id": 1,
      "name": "Sydney Noh",
      "address": "966 Software School Rd.",
      "email": "sydneynoh@mail.com"
    },
    {
      "id": 2,
      "name": "Trevor Guinn",
      "address": "123 NSS Ln",
      "email": "trevorguinn@mail.com"
    },
    {
      "id": 3,
      "name": "Steven Nagel",
      "address": "345 Somewhere St",
      "email": "stevennagel@mail.com"
    },
    {
      "id": 4,
      "name": "Ricky Bobby",
      "address": "678 IwantToGoFast Dr.",
      "email": "rickybobby@mail.com"
    },
    {
      "name": "Customer 5",
      "address": "222 Place Dr",
      "id": 5,
      "email": "customer5@mail.com"
    },
    {
      "name": "Customer 6",
      "address": "222 Road Pl",
      "id": 6,
      "email": "customer6@mail.com"
    },
    {
      "email": "billybob@mail.com",
      "name": "Billy Bob",
      "id": 7,
      "address": "888 Road Pl"
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
            
    return requested_customer