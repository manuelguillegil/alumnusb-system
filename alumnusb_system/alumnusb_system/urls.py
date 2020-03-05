from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from main import views
from CSV.views import profile_upload

urlpatterns = [
    url(r'^$', views.index, name='home'),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    url(r'^dashboard/(?P<username>[\w.@+-]+)/$', views.dashboard, name = 'dashboard'),
    path('upload-csv/', profile_upload, name="profile_upload"),
    url(r'^dashboard/(?P<username>[\w.@+-]+)/$', views.dashboard, name = 'dashboard'),
    url(r'^my_stats/(?P<username>[\w.@+-]+)/$', views.user_stats, name = 'my_stats')
]
