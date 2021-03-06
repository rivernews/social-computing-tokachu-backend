"""django_backend URL Configuration

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
from django.urls import path,include

import blog.views as blog_views
import account.views as account_views
import place.views as place_views
import api.views as api_views

from django.views.generic import RedirectView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', blog_views.PostViewSet)
router.register(r'users', account_views.UserViewSet)
router.register(r'place', place_views.PlaceViewSet)
router.register(r'pictures', api_views.PicturesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('', blog_views.home_view),
]
