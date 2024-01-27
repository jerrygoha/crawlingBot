"""
현재 Django project 의 URL 선언을 저장합니다.
Django 로 작성된 사이트의 “목차” 라고 할 수 있습니다.
URL dispatcher 에서 URL 에 대한 자세한 내용을 읽어보세요.

URL configuration for crawlingProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from . import views
from crawlingApp.view import mainPage

urlpatterns = [
    path("", views.index, name="index"),
    ##메인화면
    path("", mainPage.admin_main, name="admin_main"),
]
