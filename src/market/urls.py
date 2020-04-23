from django.urls import path
from market import views


app_name = 'market'

urlpatterns = [
    path('admin_register/', views.AdminRegisterView.as_view(), name='admin_register'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('customer_register/', views.CustomerRegisterView.as_view(), name='customer_register'),
]
