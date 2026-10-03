"""
URL configuration for helpdesk project.

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
from django.urls import path
from system.views import Register,Logout,TicketCreateList,TicketUpdateDeleteRetrieve,TicketSummary
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/',Register.as_view()),
    path('api/login/',ObtainAuthToken.as_view()),
    path('api/logout/',Logout.as_view()),
    path('api/tickets/',TicketCreateList.as_view()),
    path('api/tickets/<int:pk>/',TicketUpdateDeleteRetrieve.as_view()),
    path('api/summury/',TicketSummary.as_view()),
    




]
