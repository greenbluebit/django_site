from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Movie, Show
from django.shortcuts import get_object_or_404
from django.db.models import Q


def index(request):
    latest_movie_list = Movie.objects.order_by('-release_date')[:12]
    latest_shows_list = Show.objects.order_by('-release_date')[:12]
    template = loader.get_template('fresh_tomatoes/index.html')
    context = RequestContext(request, {'latest_movie_list':latest_movie_list,'latest_shows_list':latest_shows_list})
    #return render(request, 'fresh_tomatoes/index.html', {'latest_movie_list':latest_movie_list})
    return HttpResponse(template.render(context))

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    template = loader.get_template('fresh_tomatoes/detail.html')
    context = RequestContext(request, {'movie':movie})
    #return render(request, 'fresh_tomatoes/detail.html', {'movie':movie})
    return HttpResponse(template.render(context))

# brings shows and movies which have title or plot LIKE searched value
def search(request, searched):
    found_movies_list = Movie.objects.filter(Q(title_text__contains=searched) | Q(plot__contains=searched))
    found_shows_list = Show.objects.filter(Q(title_text__contains=searched) | Q(plot__contains=searched))
    template = loader.get_template('fresh_tomatoes/index.html')
    context = RequestContext(request, {'latest_movie_list':found_movies_list,'latest_shows_list':found_shows_list})
    return HttpResponse(template.render(context))