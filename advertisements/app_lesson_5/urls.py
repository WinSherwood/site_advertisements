from django.urls import path

from .views import index, top, post, register, login, profile, advertisement
urlpatterns = [
    path("", index, name="/"),
    path("top-sell", top, name="top"),
    path("post", post, name="post"),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("profile", profile, name="profile"),
    path("advertisement", advertisement, name="advertisement"),
]