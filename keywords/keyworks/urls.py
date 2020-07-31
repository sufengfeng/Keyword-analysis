"""keyworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from keyworks import settings
from webdev import views

urlpatterns = [

    url(r'^index$', views.index),
    url(r'^signup$', views.signup),
    url(r'^login$', views.login),
    url(r'^userOptions$', views.userOptions),
    url(r'^userPanel$', views.userPanel),
    url(r'^save_context$', views.save_context), #保存context
    url(r'^open_title$', views.open_title), #打开context
    url(r'^delete_title$', views.delete_title), #删除context
    url(r'^get_nearby$', views.get_nearby), #删除context



    url(r'^index.html$', views.index),
    url(r'^signup.html$', views.signup),
    url(r'^login.html$', views.login),
    url(r'^userOptions.html$', views.userOptions),
    url(r'^userPanel.html$', views.userPanel),
    url(r'^test.html$', views.test),

    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index)
    #url(r'^name/',include('webdev.urls'))
]
