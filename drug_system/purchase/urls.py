from django.urls import path

from . import views

app_name = 'purchase'

urlpatterns = [
    path('purchase/', views.purchase, name='purchase'),
    path('submit/', views.submit, name='submit'),
    path('make/', views.make, name='make'),
    path('query/', views.query, name='query'),
    path('query_detail/<int:purchase_id>/', views.query_detail, name='query_detail'),
    path('accept/<int:purchase_id>/', views.accept, name='accept'),
    path('deny/<int:purchase_id>/', views.deny, name='deny'),
]
