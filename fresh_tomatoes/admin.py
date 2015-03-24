from fresh_tomatoes.models import Movie
from fresh_tomatoes.models import Show
from fresh_tomatoes.models import MoviePerson
from fresh_tomatoes.models import ShowPerson
from django.contrib import admin

# Register admin models here.
class MoviePersonInline(admin.TabularInline):
    model = MoviePerson
    extra = 3

class ShowPersonInline(admin.TabularInline):
    model = ShowPerson
    extra = 3

# Customize what is the most important to show.
class MovieAdmin(admin.ModelAdmin):
    fieldsets = [('Main', {'fields':['title_text', 'plot', 'poster','trailer_youtube_url','release_date']}),
        ('Secondary', {'fields':['rating', 'available_imax','available_3d', 'duration', 'budget', 'trivia', 'goofs'],'classes':['collapse']})]
    inlines = [MoviePersonInline]
    list_display = ('title_text', 'release_date')
    list_filter = ['release_date']
    search_fields = ['title_text']
admin.site.register(Movie, MovieAdmin);


class ShowAdmin(admin.ModelAdmin):
    fieldsets = [('Main', {'fields':['title_text', 'plot', 'poster','network','release_date']}),
        ('Secondary', {'fields':['seasons','available_imax','available_3d', 'rating'],'classes':['collapse']})]
    inlines = [ShowPersonInline]
    list_display = ('title_text', 'release_date')
    list_filter = ['release_date']
    search_fields = ['title_text']

admin.site.register(Show, ShowAdmin);

