from django.shortcuts import render
from django.http import HttpResponse


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
    return render(request, 'master_view/base.html', {'title':title})


