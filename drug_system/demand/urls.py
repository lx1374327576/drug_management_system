from django.urls import path

from . import views

app_name = 'demand'

urlpatterns = [
    path('demand/', views.demand, name='demand'),
    path('submit/', views.submit, name='submit'),
    path('make/', views.make, name='make'),
    path('query/', views.query, name='query'),
    path('query/<int:page_id>/', views.query_page, name='query_page'),
    path('accept/<int:demand_id>/', views.accept, name='accept'),
    path('deny/<int:demand_id>/', views.deny, name='deny'),
    path('query_detail/<int:demand_id>/', views.query_detail, name='query_detail'),
]
