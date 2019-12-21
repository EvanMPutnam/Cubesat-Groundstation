from django.db import models

# Create your models here.
class Dataref(models.Model):
    data_ref_name = models.CharField(max_length=50)
    data_ref_project = models.CharField(max_length=50)
    json_data = models.TextField()
    class Meta:
        unique_together = (('data_ref_name', 'data_ref_project'))