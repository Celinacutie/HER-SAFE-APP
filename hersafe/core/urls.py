# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login" ),
    path("reporting/",views.reporting_view, name="reporting")
]