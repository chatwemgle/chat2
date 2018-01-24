from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^home/$', views.Home, name='home'),

    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),
    url(r'^$', views.Prelogin, name='home'),
    url(r'^deletemessages/$', views.DeleteMessages, name='deletemessages'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]