from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.StandingsListView.as_view(), name='standings-list'),
]
