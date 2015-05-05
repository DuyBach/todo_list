from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='polls'),
    # /polls/impressum
    url(r'^impressum/$', views.impressum, name='impressum'),
    # /polls/add
    url(r'^add/$', views.add, name='add'),
    # ex: /polls/5 Miles/edit, /polls/Run/edit
    url(r'^(?P<todo>[A-Za-z0-9]+)/edit/$', views.detail, name='detail'),
]