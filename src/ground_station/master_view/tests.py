from django.test import TestCase
from django.test import Client
import requests


def stress_test(data_ref_name, data_ref_proejct, append_value):
    src = "http://127.0.0.1:8000/master_view/api/append_data_to_array_maintain"
    name = 'data_ref_name'
    project = 'data_ref_project'
    data_val = 'data_val'
    
    data = {name: data_ref_name, project: data_ref_proejct, "data_val": append_value}
    r = requests.post(src, json=data)
    print(r.content)


# Create your tests here.
if __name__ == "__main__":
    stress_test('Altitude Data','Project_1', 5)
    #src = "http://127.0.0.1:8000/master_view/create_dataref"
    #name = 'data_ref_name'
    #project = 'data_ref_project'

    #example_df_name = "test_name1"
    #example_project = "test_project1"

    #data = {name: example_df_name, project: example_project}
    #r = requests.post(src, json=data)
    #print(r.content)