"""ProyectoSol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from SolApp.views import *



urlpatterns = [
    path('', mostrar_index),
    path('crear_suscriptor/', crear_suscriptor, name= 'suscriptor'),
    path('crear_posteo/', crear_posteo, name= 'posteo'),
    path('buscar_posteo/', buscar_posteo, name= 'buscar posteo'),
    path('buscar_suscriptor/', buscar_suscriptor, name= 'buscar suscriptor'),
    path('we_opinion/', we_opinion, name= 'we opinion'),
    path('the_car_opinion/', the_car_opinion, name= 'the car opinion'),
    path('wotp_opinion/', wotp_opinion, name= 'wotp opinion'),
    path('rhcp_opinion/', rhcp_opinion, name= 'rhcp opinion'),
    path('phoenix_opinion/', phoenix_opinion, name= 'phoenix opinion')
]