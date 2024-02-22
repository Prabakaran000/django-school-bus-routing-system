from django.db import models

from django.db import models

class SchoolBus(models.Model):
    bus_number = models.CharField(max_length=100,  primary_key=True)
    route_number = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, default='')
    std_name = models.CharField(max_length=50, default='')
    std_age = models.CharField(max_length=50, default='')
    father_name = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.bus_number


class Routes(models.Model):
    route_number = models.CharField(max_length=100,  primary_key=True)
    start_from = models.CharField(max_length=50)
    end_from = models.CharField(max_length=100)

    def __str__(self):
        return self.route_number


class Students(models.Model):
    student_id = models.CharField(max_length=100,  primary_key=True)
    std_name = models.CharField(max_length=50)
    std_age = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.student_id

