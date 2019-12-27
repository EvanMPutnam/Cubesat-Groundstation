from django.urls import path
from . import views


urlpatterns = [
    path("/", views.template_example),
    path('/<project_name>', views.template_example),
    path("/api/create_dataref", views.create_dataref),
    path("/api/create_project", views.create_project),
    path("/api/get_dataref", views.get_dataref),
    path("/api/modify_data", views.modify_data)
]