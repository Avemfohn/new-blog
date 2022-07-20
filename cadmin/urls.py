from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    url(r'^post/add/$', views.post_add, name='post_add'),
    url(r'^post/update/(?P<pk>[\d]+)/$',
        views.post_update, name='post_update'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='cadmin/login.html'), name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(template_name='cadmin/logout.html'), name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/login/$', views.login,
        {'template_name': 'blog/login.html'}, name='login'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name='cadmin/password_change.html'),
        name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='cadmin/password_change_done.html'),
    #      name='password_change_done'),

]
