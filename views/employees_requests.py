EMPLOYEES = [
    {
      "id": 1,
      "name": "Emma Beaton",
      "locationId": "4"
    },
    {
      "id": 2,
      "name": "Samantha Smith",
      "locationId": 2
    },
    {
      "id": 3,
      "name": "Bob Smith",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Julie Jules",
      "locationId": 1
    },
    {
      "id": 5,
      "name": "Brian Brians",
      "locationId": "4"
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
  
def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee