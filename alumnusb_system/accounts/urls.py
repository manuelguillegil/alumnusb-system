from django.urls import path
from . import views as account_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('',account_views.indexView,name="home"),
	path('dashboard/',account_views.dashboardView,name="dashboard"),
	path('login/',LoginView.as_view(),name="login_url"),
	path('register/',account_views.registerView,name="register_url"),
	path('test_luis/',account_views.registerView,name="register_url"),
	path('logout/',LogoutView.as_view(next_page="home"),name="logout")
]