from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/',views.employee_form,name="update"),
    path('', views.employee_form, name="form"),
    path('list/', views.employee_list, name="list"),
    path('delete/<int:id>/', views.employee_delete, name='Delete')
    
]