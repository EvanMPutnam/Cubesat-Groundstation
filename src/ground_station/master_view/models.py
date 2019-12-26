from django.db import models


#Project information
class Project(models.Model):
    project_name = models.CharField(max_length=50, primary_key=True, unique=True)

#Dataref information.
class Dataref(models.Model):

    DOUBLE_ARR = "Double_Arr"
    INTEGER_ARR = "Integer_Arr"
    DOUBLE = "Double"
    INT = "Int"
    TYPE_OF_DATA = [
        (DOUBLE_ARR, DOUBLE_ARR),
        (INTEGER_ARR, INTEGER_ARR),
        (DOUBLE, DOUBLE),
        (INT, INT)
    ]

    data_ref_name = models.CharField(max_length=50, db_index=True)
    data_ref_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    json_data = models.TextField()
    order_weight = models.IntegerField(default=1)
    type_of_data = models.CharField(choices=TYPE_OF_DATA, default=INT, max_length=11)

    class Meta:
        unique_together = (('data_ref_name', 'data_ref_project'))

