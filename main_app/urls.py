from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.queero_index, name='index'),
    path('queeroes/<int:queero_id>/', views.queero_detail, name='detail'),

]