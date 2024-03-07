
from django.urls import path
from webapp import views

urlpatterns = [
    
    path('', views.indexView, name=""),
    path('register/', views.register, name="register"),
    path('my-login/', views.my_login, name='my-login'), 
    path('my-logout/', views.user_logout, name='my-logout'), 
    
    path('dashboard/', views.dashboard, name='dashboard'),   
    path('create-customer/',views.CreateCustomer, name='create-customer'),
    path('update-customer/<int:pk>',views.UpdateCustomer, name='update-customer'),
    path('record/<int:pk>',views.SinglurCustomer, name='record'),
    path('delete/<int:pk>',views.DeleteCustomer, name='delete'),

]   

