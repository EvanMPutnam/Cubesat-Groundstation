from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt, csrf_protect

from master_view.models import Dataref
from master_view.models import Project


import json

'''
Steps to add new view:
    1) Place url in urls.py
    2) If first template in app, then add template location to settings.py
    3) Create function and do any logic you need
'''

'''
Steps TODO
    1) Create model.
        - Have model be able to handle different types of data/displays
    2) Have HTML parse the display OBJ and display the data.
        - Have an ajax method that queries the database and updates everything
'''


#######################################################
#   Description:    Main view for application
#
#######################################################
def index_view(request):
    return HttpResponse("<h1>Page was found</h1>")




#######################################################
#   Description:    Example of a template
#
#######################################################
def template_example(request):
    title = "Hello Template!"
    return render(request, 'master_view/base.html', {'title':title})


#######################################################
#   Description:    Update a dataref on the screen.
#
#######################################################
def update_data(request):
    pass


#######################################################
#   Description:    Update a dataref on the screen.
#
#######################################################
@csrf_exempt
def create_dataref(request):
    status_r = {'status': 'Success'}
    if request.method == 'POST':
        try:
            #Loads the json.
            data = json.loads(request.body)
            #Gets the needed parameters.
            name = data['data_ref_name']
            project = data['data_ref_project']
            project = Project.objects.filter(project_name=project)[0]
            json_data = data['json_data']
            order_weight = data['order_weight']
            #Create object and save!
            data_ref_obj = Dataref(data_ref_name=name, data_ref_project=project, 
                                    json_data=json_data, order_weight=order_weight)
            data_ref_obj.save()
            print("Success in creating dataref.")
            return JsonResponse(status_r)
        except Exception as e:
            status_r = {'status':'ERROR -> ' + str(e)}
            return JsonResponse(status_r)
    else:
        status_r = {'status':'Invalid'}
        return JsonResponse(status_r)


#######################################################
#   Description:    Create a project.
#
#######################################################
@csrf_exempt
def create_project(request):
    status_r = {'status': 'Success'}
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            project = data['project_name']
            project_obj = Project(project_name=project)
            project_obj.save()
            print("Success in creating new project.")
            return JsonResponse(status_r)
        except Exception as e:
            status_r = {'status':'ERROR -> ' + str(e)}
    else:
        status_r = {'status':'Invalid'}
        return JsonResponse(status_r)