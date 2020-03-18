from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from main import views
from CSV.views import profile_upload

# Por favor tratar con carino estos url
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

    url(r'^admin/', admin.site.urls),
    path('upload-csv/', profile_upload, name="profile_upload"),

    url(r'^$', views.index, name='home'),
    url(r'^dashboard/(?P<username>[\w.@+-]+)/$', views.dashboard, name = 'dashboard'),

    path('accounts/', include('accounts.urls')),

    url(r'^prueba_logros/(?P<username>[\w.@+-]+)/$', views.achievements, name = 'achievements'),
    url(r'^my_stats/(?P<username>[\w.@+-]+)/$', views.user_stats, name = 'my_stats'),
    url(r'^my_achievements/(?P<username>[\w.@+-]+)/$', views.user_achievs, name = 'my_achievs')
]
