from django.urls import path
from . import views

urlpatterns = [

    path('', views.gallery),

    path('contact/', views.contact),

]