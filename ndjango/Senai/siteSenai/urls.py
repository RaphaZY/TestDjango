from django.urls import path

from siteSenai.views import *

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login")
]