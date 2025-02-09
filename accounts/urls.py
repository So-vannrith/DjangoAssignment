from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    path('', views.Index, name='home'),
    path('Home', views.Index, name='home'),
    path('About', views.about),
    path('Services', views.service),
    path('Contact', views.contact),
    path('Product', views.product , name='Product'),
    path('Gallery', views.gallery, name='Gallery'),
    
]