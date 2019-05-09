from django.urls import path

from . import views

app_name = 'purchase'

urlpatterns = [
    path('purchase/', views.purchase, name='purchase'),
]
