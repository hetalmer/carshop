from django.urls import path
from . import views

urlpatterns=[
    path('login',views.login1,name='login-page'),
    path('register',views.register,name='register-page'),
    path('dashboard',views.dashboard,name='dashboard-page'),
    path('logout',views.logout1,name='logout-page'),
    path('<int:id>',views.ddelete,name='dashboard-delete'),
]