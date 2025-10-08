"""
URL configuration for mirko_incordatore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("prenotazioni.urls")), # include le rotte dell'app prenotazioni
    path('api/auth/register/', include("utenti.urls")), # include le rotte dell'app utenti relativi alla registrazione
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Endpoint per ottenere il token JWT
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Endpoint per refreshare il token JWT
]
