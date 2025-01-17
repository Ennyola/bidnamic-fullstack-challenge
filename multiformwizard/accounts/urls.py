from django.urls import path
from .views import login_view, signup, logout_view

app_name = "accounts"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", logout_view, name="logout"),
]
