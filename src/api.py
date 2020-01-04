'''
NOTE: This is VERY much still a work in progress.  
This likely will not be done and finalized until the later stages of the project.

'''
#For API Use
import requests
import random

#For testing use.
import time


BASE_URL = r'http://127.0.0.1:8000/master_view/'
UPDATE_DATAREF_SRC = "http://127.0.0.1:8000/master_view/api/modify_data"

#Operation types for data manipulation
APPEND_OP = "APPEND"
REPLACE_OP = "REPLACE"


#Method for creating datarefs (Current supported datarefs are int, int_arr, double, double_arr)
#User needs to pre-process the json data
def create_dataref(name, project_name, order_weight=1, json_data=r"{\"data_val\": 0}"):
    #URL
    src = BASE_URL + "create_dataref"
    #Fields
    name_field = 'data_ref_name'
    project_field = 'data_ref_project'
    json_data_field = "json_data"
    order_weight_field = "order_weight"
    if 'data_val' not in json_data:
        raise Exception("Error: No data_val item inside of json data.")
    #Create JSON
    data = {name_field: name, project_field: project_name, 
            json_data_field: json_data, 
            order_weight_field: order_weight}
    #Request
    r = requests.post(src, json=data)
    print(r.content)



#Methods for creating projects
def create_project(project_name):
    #URL
    src = BASE_URL + "create_project"
    #Fields
    project_name_field = "project_name"
    #Create JSON
    data = {project_name_field: project_name}
    #Request
    r = requests.post(src, json=data)
    print(r.content)




def update_data(data_ref_name, data_ref_proejct, value_to_add, type_of_op = APPEND_OP, debug = False):
    #Paremeter names in the database
    name = 'data_ref_name'
    project = 'data_ref_project'
    data_val = 'data_val'
    modification = 'modification'
    
    #Format the data to send
    data = {name: data_ref_name, 
            project: data_ref_proejct, 
            data_val: str(value_to_add),
            modification: type_of_op}

    #Send and print request
    r = requests.get(UPDATE_DATAREF_SRC, params=data)
    print(debug)
    if debug:
        print(r.content)



# Create your tests here.
if __name__ == "__main__":
    while True:
        update_data('Airspeed Data','Project_1', random.randint(200, 400), REPLACE_OP)
        update_data('Altitude Data','Project_1', random.randint(0, 100))
        update_data('Some Other Graph','Project_1', random.randint(0, 100))
        update_data('Some Other Data Field','Project_1', random.randint(0, 100))
        time.sleep(10)