import requests


BASE_URL = r'http://127.0.0.1:8000/master_view/'



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

if __name__ == "__main__":
    create_project("Project Test 2")
    #Creates a
    create_dataref("hello_data", "Project Test 2", 
                    2, r"{Hello: 1, name:'Hello World'}")