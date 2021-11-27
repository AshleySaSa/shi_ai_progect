"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from .user import vertify, tes, login, fu, real_name
from .score import get_all_score, enter_score, store_mp3_and_getai_score
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login.login.as_view()),
    path('vertify/', vertify.vertify.as_view()),
    path('tes/', tes.tes.as_view()),
    path('get_all_score/',get_all_score.get_all_score.as_view()),
    path('renew/', fu.renew.as_view()),
    path('real_name/',real_name.real_name.as_view()),
    path('enter_score/',enter_score.enter_score.as_view()), # store_mp3_and_getai_score store_score_mp3
    path('store_mp3_and_getai_score/',store_mp3_and_getai_score.store_mp3_and_getai_score.as_view())

]
