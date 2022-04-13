LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8522 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    },
    {
      "name": "Nashville East",
      "address": "444 East Dr",
      "id": 3
    },
    {
      "id": 4,
      "name": "Nashville West",
      "address": "777 West Ave"
    }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None
    
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
            
    return requested_location