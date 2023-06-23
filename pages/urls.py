from django.urls import path 
from .views import * 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('portfolio/', Portfolio.as_view(), name='portfolio'),
    path('we-do/', We_Do.as_view(), name='we_do'),
]