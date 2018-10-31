"""boosup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from kucun import views as kucun_views
from kucun import urls as kucun_urls
from base import urls as base_urls
from career import urls as career_urls
from performance import urls as performance_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kucun/', include(kucun_urls)),
    path('',include(base_urls)),
    path('career/', include(career_urls)),
    path('performance/', include(performance_urls)),
]
