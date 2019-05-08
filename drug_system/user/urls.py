from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('<int:id>/<str:query_name>/', views.query, name='query'),
]
