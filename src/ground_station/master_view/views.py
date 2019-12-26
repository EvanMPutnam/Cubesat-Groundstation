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
    data_refs = Dataref.objects.filter(data_ref_project="Project_1")
    for data_ref in data_refs:
        data_ref.json_data = json.loads(data_ref.json_data)
    return render(request, 'master_view/base.html', {'title':title, "data_refs": data_refs})


#######################################################
#   Description:    Update a dataref on the screen.
#
#######################################################
def update_data(request):
    pass


@csrf_exempt
#######################################################
#   Description:     Get the information relevant to 
#                    a dataref.
#
#######################################################
def get_dataref(request):
    if request.method == 'GET':
        try:
            data_ref_project = request.GET['data_ref_project']
            data_ref_name = request.GET['data_ref_name']
            dataref = Dataref.objects.filter(data_ref_project=data_ref_project, data_ref_name=data_ref_name)[0]
            json_data = json.loads(dataref.json_data)
            status_r = {'status': 'Success', 'dataref': json_data, 'type_of_data': dataref.type_of_data}
            return JsonResponse(status_r)
        except Exception as e:
            status_r = {'status':'ERROR -> ' + str(e)}
            return JsonResponse(status_r)
    else:
        status_r = {'status': 'Error'}
        return JsonResponse(status_r)




#######################################################
#   Description:    Create a dataref.
#                       TODO: Add refresh_time
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
            refresh_time = data['refresh_time']
            #Create object and save!
            data_ref_obj = Dataref(data_ref_name=name, data_ref_project=project, 
                                    json_data=json_data, order_weight=order_weight,
                                    refresh_time=refresh_time)
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