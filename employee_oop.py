import employee_app
import json

class Employee:

    def __init__(self, emp_id, first_name, last_name):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Employee ID: {self.emp_id} - Employee First Name: {self.first_name} - Employee Last Name: {self.last_name}"

def save_to_json():
    temp_dict_of_dict = {}
    for employee_id in all_employees_dict:
        employee_obj = all_employees_dict[employee_id]
        employee_dict = employee_obj.__dict__
        temp_dict_of_dict[employee_id] = employee_dict

    with open("data.json", "w") as data_file:
        json.dump(temp_dict_of_dict, data_file)

def load_from_json():
    global all_employees_dict
    temp_dict_of_dict = {}
    try:
        with open("data.json", "r") as data_file:
            temp_dict_of_dict = json.load(data_file)
    except:
        print("The file data1.json doesn't exist")

    print(temp_dict_of_dict)

    for employee_id_key in temp_dict_of_dict:
        employee_id = temp_dict_of_dict[employee_id_key]['emp_id']
        employee_first_name = temp_dict_of_dict[employee_id_key]['first_name']
        employee_last_name = temp_dict_of_dict[employee_id_key]['last_name']

        employee_obj = Employee(employee_id, employee_first_name, employee_last_name)
        all_employees_dict[employee_id] = employee_obj

if __name__ == "__main__":
    all_employees_dict = {}
    load_from_json()
    while True:
        option = employee_app.read_option()

        if option == "add":
            print("The user wants to add an Employee")
            employee_id = employee_app.read_employee_id()
            employee_first_name = employee_app.read_first_name()
            employee_last_name  = employee_app.read_last_name()

            employee_object = Employee(employee_id, employee_first_name, employee_last_name)
            all_employees_dict[employee_id] = employee_object
            save_to_json()
            print(all_employees_dict)

        elif option == "remove":
            print("The user wants to remove an Employee")
            employee_id = employee_app.read_employee_id()
            del all_employees_dict[employee_id]

        elif option == "list":
            print("The user wants a list of the employees")
            for employee_id in all_employees_dict:
                employee_obj = all_employees_dict[employee_id]
                print(employee_obj)

        elif option == "exit":
            print("Thanks, see you later")
            break

        elif option == "save":
            print("The data will ba saved to JSON file")
            save_to_json()

        elif option == "load":
            print("Th data will be loaded from a JSON file")
            load_from_json()
        else:
            print("Uknown option")