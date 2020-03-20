from django.urls import path
from django.conf.urls import url
from . import views as accounts_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	url(r'^personal_data/(?P<username>[\w.@+-]+)/$', accounts_views.user_data, name = 'user_data'),

    url(r'^personal_data/edit/(?P<username>[\w.@+-]+)/$', accounts_views.edit_user_data, name = 'edit_user_data'),
    url(r'^personal_data/edit_picture/(?P<username>[\w.@+-]+)/$', accounts_views.edit_user_picture, name = 'edit_user_picture'),

	url(r'^login/', LoginView.as_view(), name = 'login_url'),

	url(r'^register/', accounts_views.registerView, name = "register_url"),

	url(r'^logout/', LogoutView.as_view(next_page="home"), name = "logout")
]