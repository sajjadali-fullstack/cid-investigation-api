"""
URL configuration for paginationProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('criminals-api/', views.CriminalListView.as_view(), name='criminal-list'),
    path('cases-api/', views.CaseListView.as_view(), name='case-list'),
    path('evidences-api/', views.EvidenceListView.as_view(), name='evidence-list'),
    path('officers-api/', views.OfficerListView.as_view(), name='officer-list'),
    path('witnesses-api/', views.WitnessListView.as_view(), name='witness-list'),

]
