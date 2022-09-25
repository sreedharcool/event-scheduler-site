from django.urls import include, re_path
from scmapp import views

app_name = 'scmapp'

urlpatterns = [

    re_path(r'^$',views.index,name='admin_home'),
    re_path(r'^admin_event',views.admin_event,name='admin_event'),

    re_path(r'^update_event/(?P<id>\d+)/$',views.update_event,name='update_event'),
    re_path(r'^db_update_event/(?P<id>\d+)/$',views.db_update_event,name='db_update_event'),
    re_path(r'^db_delete_event/(?P<id>\d+)/$',views.db_delete_event,name='db_delete_event'),

    re_path(r'^add_event',views.add_event,name='add_event'),
    re_path(r'^db_add_event',views.db_add_event,name='db_add_event'),

    
]
