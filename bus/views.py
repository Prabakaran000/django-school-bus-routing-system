from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import SchoolBus, Routes, Students
from .forms import SchoolBusForm, RoutesForm, StudentsForm

def home(request):
    return render(request, 'index.html')

def bus_list(request):
    buses = SchoolBus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})

def route_list(request):
    routes = Routes.objects.all()
    return render(request, 'route_list.html', {'routes': routes})

def students_list(request):
    students = Students.objects.all()
    return render(request, 'students_list.html', {'students': students})

def bus_create(request):
    if request.method == 'POST':
        form = SchoolBusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = SchoolBusForm()
    return render(request, 'bus_form.html', {'form': form})

def bus_update(request, pk):
    bus = get_object_or_404(SchoolBus, pk=pk)
    if request.method == 'POST':
        form = SchoolBusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = SchoolBusForm(instance=bus)
    return render(request, 'bus_form.html', {'form': form})

def bus_delete(request, pk):
    bus = get_object_or_404(SchoolBus, pk=pk)
    if request.method == 'POST':
        bus.delete()
        return redirect('bus_list')
    return render(request, 'bus_confirm_delete.html', {'bus': bus})

def bus_list(request):
    buses = SchoolBus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})

def add_bus(request):
    if request.method == 'POST':
        form = SchoolBusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')  # Redirect to the bus list page after adding the bus
    else:
        form = SchoolBusForm()
    return render(request, 'add_bus.html', {'form': form})

def add_route(request):
    if request.method == 'POST':
        form = RoutesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route_list')  # Redirect to the bus list page after adding the bus
    else:
        form = RoutesForm()
    return render(request, 'add_routes.html', {'form': form})

def add_students(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')  # Redirect to the bus list page after adding the bus
    else:
        form = StudentsForm()
    return render(request, 'add_students.html', {'form': form})