"""
URL configuration for library_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path , include
from app import views

urlpatterns = [
    path('', views.register , name='register'),
    path('login/',views.loginpage, name='loginpage'),
    path('home/',views.home , name='home'),
    path('book/',views.book, name='book'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('account/',views.acc, name='acc'),
    path('admin/', admin.site.urls),
]
