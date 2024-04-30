from django.urls import path

from siteTrilhas.views import *

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login")
]