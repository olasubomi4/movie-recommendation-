from django.conf.urls import url
from django.urls import path,include
from . import views
from django.contrib import *
#from blog.views import HomePageView,test
from .views import test

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login_user, name='login'),
	url(r'^logout/$', views.logout_user, name='logout'),
	url(r'^register/$', views.reg_user, name='register'),
	url(r'^search/$', views.search, name='search'),
	url(r'^main/$', views.main, name='main'),

	path('search/movie/', test.as_view(), name='original_title'),



   # path('home/', HomePageView.as_view(), name='home'),
   # #path('post/', CreatePostView.as_view(), name='add_post') ,#





]
