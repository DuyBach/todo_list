from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='polls'),
    # ex: /polls/5 Miles/, /polls/Run/
    url(r'^(?P<todo>[A-Za-z0-9]+)/$', views.detail, name='detail'),
]