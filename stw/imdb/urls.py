from django.conf.urls import url
from . import views
urlpatterns = [
	# /
	url(r'^$', views.index, name='index'),
	# /movie/5/
	url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie'),
	# /movie/5/comment
	url(r'^movie/(?P<movie_id>[0-9]+)/comment/$', views.movie_comment, name='movie'),
]
