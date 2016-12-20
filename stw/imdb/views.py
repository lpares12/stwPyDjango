from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import Movie, Comment
from .forms import CommentForm

# Create your views here.
def index(request):
	return HttpResponse('<h1>Welcome!</h1>')

def movie_detail(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	return render(request, 'movie.html', {'movie':movie})

def movie_comment(request, movie_id):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			movie_obj = get_object_or_404(Movie, pk=movie_id)
			comment = Comment(movie=movie_obj, name=data['name'], text=data['comment'])
			comment.save()
			return HttpResponseRedirect('/imdb/movie/' + movie_id + '/')
		else:
			return HttpResponseBadRequest('Fill all the spaces')
	else:
		return HttpResponseBadRequest('Only POST')
