from django.test import TestCase
from django.test import Client
import requests

# Create your tests here.
if __name__ == "__main__":
    src = "http://127.0.0.1:8000/master_view/create_dataref"
    name = 'data_ref_name'
    project = 'data_ref_project'

    example_df_name = "test_name1"
    example_project = "test_project1"

    data = {name: example_df_name, project: example_project}
    r = requests.post(src, json=data)
    print(r.content)