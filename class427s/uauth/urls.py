from django.conf.urls import url
from django.contrib.auth.views import login, logout

from uauth import views


urlpatterns = [
    url(r'^regist/', views.regiter),
    url(r'^login/$', views.my_login),
    url(r'^logout/', views.logout),
    url(r'^dj_login/', views.djlogin),
    url(r'^dj_regist', views.djregist),
    url(r'^dj_logout', views.djlogout)
]