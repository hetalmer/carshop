from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home-page'),
    path('contact',views.contact,name='contact-page'),
    path('about',views.about,name='about-page'),
    path('services',views.services,name='services-page')
]
