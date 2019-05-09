from django.urls import path

from . import views

app_name = 'demand'

urlpatterns = [
    path('demand/', views.demand, name='demand'),
    path('submit/', views.submit, name='submit'),
]
