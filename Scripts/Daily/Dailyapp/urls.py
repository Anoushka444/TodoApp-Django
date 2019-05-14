from django.conf.urls import url
from django.contrib import admin
from Dailyapp import views

app_name = 'Dailyapp'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

#   url(r'^detail/', views.detail, name = 'detail' ),
#   url(r'^admin/', admin.site.urls),
]
