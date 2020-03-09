from django.db import models

# Create your models here.
from viewflow.models import Process


class SampleProcess(Process):

    start_field = models.CharField(max_length=25, default='')
    update_one = models.CharField(max_length=25, default='')
    update_two = models.CharField(max_length=25, default='')
