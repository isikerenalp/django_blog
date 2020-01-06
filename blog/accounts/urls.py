from django.conf.urls import url, include
# from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('signup/', views.signup, name="signup"),
    url(r'^login/$', views.signin, name="login"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
]
