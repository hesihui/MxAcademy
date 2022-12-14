"""MxAcademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.views.static import serve

import xadmin

from apps.users.views import LoginView, LogoutView
from apps.organizations.views import OrgView
from MxAcademy.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

    # config uploaded file url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # organization urls config
    url(r'^org/', include(('apps.organizations.urls', "organizations"), namespace="org")),

    # User operations urls config
    url(r'^op/', include(('apps.operations.urls', "operations"), namespace="op")),

    # course urls config
    url(r'^course/', include(('apps.courses.urls', "courses"), namespace="course")),

    # user center urls config 
    url(r'^users/', include(('apps.users.urls', "users"), namespace="users")),

]
