from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/<str:query_name>', views.query, name='query'),
]
