from django.urls import path
from .views import*
app_name='Users'

urlpatterns=[

     path('login/',login_request, name='login'),
     path('home_view',home_view, name='home_view'),
     path('manager',manager, name='manager_dashboard'),
     path('customer',customer, name='customer_dashboard'),

     # path('Manager_register/',Manager_register.as_view(), name='ManagerRegister'),
     # path('register/',customer_register.as_view(), name='customer_register'),
     # path('password_reset/',password_reset, name='password_reset'),
     path('logout/',logout_view, name='logout'),
]
