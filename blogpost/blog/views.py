import imdb
import pandas as pd
import numpy as np
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import RequestContext, Context
from .models import movies6
import pandas as pd
import numpy as np
from django.views import View

#from .forms import PostForm # new
#from .models import Post
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from blog.models import movies, links
from django.db.models import Q
from .forms import RegistrationForm
import pandas as pd
from .recommendation import *

from django.views.generic import ListView
#from .models import Post

import itertools
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	context = {
		'user': request.user,
		}
	return render(request,'index.html', context)

def login_user(request):
	template = 'login.html'
	state="Please fill in your credentials"
	log = False
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "Logged in!"
				log = True
				return HttpResponseRedirect('/')
			else:
				state = "Not registered user"
		else:
			state = "Incorrect username or password!"
	context={
		'state': state,
		'log': log
		}
	return render(request, template, context )

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/') 

@login_required
def search(request):
	query = "no results found"
	neighbors = []
	recommended = []
	results = []
	posters = []
	mvies = []


	show_results = False
	if request.GET:
		query = request.GET['query']
		results = movies6.objects.filter(original_title__icontains=query)[:10]
		show_results = True
		#access = imdb.IMDb()
#	titles = []
#	covers = []
#	for i in results:
#		movie_id = links.objects.get(movie_id=i.movie_id)
#		movie = access.get_movie(str(movie.imdb_id))
#		titles.append(movie['title'])
#		covers.append(movie['cover url'])

	context={
		#'mvies': mvies,

		'results': results,
		'show_results': show_results
	}
		
	return render(request,'search.html', context)




def main(request):
	return render(request,'main.html')

def reg_user(request):
	state= ""
	template = 'register.html'
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email']
			)
			return HttpResponseRedirect('/login')
		else:
			state = "Incorrect Credentials!"
	else:
		form = RegistrationForm()
	context={'form':form, 'state':state}
	return render(request,'register.html', context)
import numpy as np
import pandas as pd
class test(View):
	def get(self,request):
		template = 'movie.html'
		query = ""
		show = []
		obj = []
		if request.GET:
			query = request.GET['query']



			df = pd.read_csv("movie_dataset.csv")


			features = ['keywords','cast','genres','director']

			def combine_features(row):
				return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']

			for feature in features:
				df[feature] = df[feature].fillna('')  # filling all NaNs with blank string

			df["combined_features"] = df.apply(combine_features,axis=1)  # applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column

			 # applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column
			df.iloc[0].combined_features

			cv = CountVectorizer()  # creating new CountVectorizer() object
			count_matrix = cv.fit_transform(df["combined_features"])
			cosine_sim = cosine_similarity(count_matrix)

			def get_title_from_index(index):
				return df[df.index == index]["title"].values[0]

			def get_index_from_title(title):
				return df[df.title == title]["index"].values[0]

	

			movie_user_likes = query
			movie_index = get_index_from_title(movie_user_likes)
			similar_movies = list(enumerate(cosine_sim[movie_index]))  # accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
			sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

			print("Top 5 similar movies to " + movie_user_likes + " are:\n")
			for element in sorted_similar_movies[:10]:
				shows=(get_title_from_index(element[0]))
				show.append(shows)

			#model=Post
			#obj= get_object_or_404(model, title=show[0])
		context={
	    	
	    	'show':show,
			 'name':query,
			#'object':obj,

		}
		return render(request,'movie.html', context)




class HomePageView(View):
  def get(self, request):
	  model= Post
	  template_name='home.html'
	  obj = get_object_or_404(model,pk=3)
	  g=[]




	  context = {"object": obj}
	  return render(request, template_name, context)








#class CreatePostView(CreateView): # new
  #  model = Post
   # form_class = PostForm
    #template_name = 'post.html'
    #success_url = reverse_lazy('home')