from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index),
    url(r"^sigin$", views.sigin),
    url(r"^register$", views.register),
    url(r"^register_user$", views.register_user),
    url(r"^login$", views.login),
    url(r"^logoff$", views.logoff),
    url(r"^dashboard/admin$", views.admin),
    url(r"^dashboard$", views.dashboard),
    url(r"^users/new$", views.new),
    url(r"^add_user$", views.add_user),
    url(r"^dashboard/edit/(?P<user_id>\d+)$", views.edit),
    url(r"^dashboard/(?P<user_id>\d+)$", views.edit),
    url(r"^update_user/(?P<user_id>\d+)$", views.update_user),
    url(r"^profile$", views.profile),
    url(r"^edit_profile$", views.edit_profile),
    url(r"^dashboard/info/(?P<user_id>\d+)$", views.info),
    url(r"^dashboard/post/(?P<user_id>\d+)$", views.post),
    url(r"^dashboard/massage/(?P<post_id>\d+)/(?P<user_id>\d+)$", views.massage),
    url(r"^remove/(?P<user_id>\d+)$", views.remove),

]