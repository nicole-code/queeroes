from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.queero_index, name='index'),
    path('queeroes/<int:queero_id>/', views.queero_detail, name='detail'),
    path('queeroes/new', views.queero_new, name='newqueero'),
    path('queeroes_submit/', views.queero_create, name='createqueero'),
    path('queeroes/<int:queero_id>/delete/', views.queero_delete, name='deletequeero'),
    path('queeroes/<int:queero_id>/edit/', views.queero_edit, name='editqueero'),
    path('queeroes/<int:queero_id>/submit_update_form/', views.queero_update, name='updatequeero'),
    path('queeroes/<int:queero_id>/submit-quote/', views.add_queero_quote, name='addqueeroquote')
]