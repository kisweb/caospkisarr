from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


app_name = 'account'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile")
]