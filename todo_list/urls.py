from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^impressum/$', views.ImpressumView.as_view(), name='impressum'),
    url(r'^add/$', views.AddView.as_view(), name='add'),
    url(r'^edit/(?P<pk>[A-Za-z0-9\w|\W]+)$', views.UpdateView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>[A-Za-z0-9\w|\W]+)$', views.DeleteView.as_view(), name='delete'),
)