from . import views
from django.urls import path

urlpatterns = [
  path("ping", views.PingView.as_view()),
  path("info/space/", views.SpaceView.as_view())
]
