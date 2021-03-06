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
import event.views as event_views
import conversation.views as conversation_views
import connection.views as connection_views

from django.views.generic import RedirectView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', blog_views.PostViewSet)
router.register(r'users', account_views.UserViewSet)

router.register(r'pictures', api_views.PicturesViewSet)
router.register(r'locations', api_views.LocationViewSet)
router.register(r'tags', api_views.TagViewSet)
router.register(r'theme', api_views.ThemeViewSet)

router.register(r'place', place_views.PlaceViewSet)
router.register(r'event', event_views.EventViewSet)
router.register(r'conversation', conversation_views.ConversationViewSet)
router.register(r'user_event', connection_views.User_EventViewSet)
router.register(r'event_picture', connection_views.Event_PictureViewSet)
router.register(r'interest_list', connection_views.Interest_listViewSet)
router.register(r'user_conversation', connection_views.User_ConversationViewSet)
router.register(r'event_tag', connection_views.Event_TagViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('', blog_views.home_view),
]
