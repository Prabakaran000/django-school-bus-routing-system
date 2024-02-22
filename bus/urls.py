from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bus', views.bus_list, name='bus_list'),
    # path('bus/<str:bus_number>/', views.bus_details, name='bus_details'),
    path('bus/create/', views.bus_create, name='bus_create'),
    path('bus/<int:pk>/update/', views.bus_update, name='bus_update'),
    path('bus/<int:pk>/delete/', views.bus_delete, name='bus_delete'),
    path('buses/', views.bus_list, name='bus_list'),
    path('add_bus/', views.add_bus, name='add_bus'),
    path('routes/', views.route_list, name='route_list'),
    path('add_route/', views.add_route, name='add_route'),
    path('add_students/', views.add_students, name='add_students'),
    path('students_list/', views.students_list, name='students_list'),
    
]
 