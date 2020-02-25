from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from main import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    url(r'^dashboard/(?P<username>[\w.@+-]+)/$', views.dashboard, name = 'dashboard')
]
