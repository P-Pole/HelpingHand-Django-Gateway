"""
URL configuration for Gateway project.

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

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('charities/', views.get_charities, name='get_charities'),
    # path('charities/<str:pk>/like/', views.like_charity, name='like_charity'),
    path('transactions/', views.post_transactions, name='post_transactions'),
    path('charities/<str:pk>/', views.get_charitiesID, name='get_charitiesID'),
    path('user_auth/', views.login_auth, name="login_auth"),
    path('register_user/', views.register_user, name="register_user"),

]
