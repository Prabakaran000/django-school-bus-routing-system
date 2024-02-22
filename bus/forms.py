from django import forms
from .models import SchoolBus,Routes,Students

class SchoolBusForm(forms.ModelForm):
    class Meta:
        model = SchoolBus
        fields = ['bus_number', 'route_number', 'capacity', 'driver_name','student_id','std_name','std_age','father_name','location']
class RoutesForm(forms.ModelForm):
    class Meta:
        model = Routes
        fields = [ 'route_number', 'start_from', 'end_from']


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [ 'student_id', 'std_name', 'std_age', 'father_name', 'location']

