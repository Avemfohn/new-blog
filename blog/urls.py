from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^category/(?P<category_slug>[\w-]+)/$',
        views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<id>\d+)/(?P<post_slug>[\w\d-]+)$',
        views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^cookie/$', views.test_cookie, name='cookie'),
    url(r'^stop-tracking/$', views.stop_tracking, name='stop_tracking'),
    url(r'^track_user/$', views.track_user, name='track_user'),
    url(r'^test-delete/$', views.test_delete, name='test_delete'),
    url(r'^test-session/$', views.test_session, name='test_session'),
    url(r'^save-session-data/$', views.save_session_data, name='save_session_data'),
    url(r'^access-session-data/$', views.access_session_data,
        name='access_session_data'),
    url(r'^delete-session-data/$', views.delete_session_data,
        name='delete_session_data'),
    url(r'^lousy-login/$', views.lousy_login, name='lousy_login'),
    url(r'^lousy-secret/$', views.lousy_secret, name='lousy_secret'),
    url(r'^lousy-logout/$', views.lousy_logout, name='lousy_logout'),
]
