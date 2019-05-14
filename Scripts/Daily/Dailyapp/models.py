from django.db import models

# Create your models here.


class Task(models.Model):

    def __str__(self):
        return self.task_name

    task_name = models.CharField(max_length = 200)
    task_priority = models.CharField(max_length= 200)


