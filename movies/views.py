from django.shortcuts import render
from .forms import MovieForm
from .models import Movie

def movie_form(request):

    message = ""

    if request.method == "POST":

        form = MovieForm(request.POST)

        if form.is_valid():

            movie_name = form.cleaned_data['movie_name']
            release_year = form.cleaned_data['release_year']

            Movie.objects.create(
                movie_name=movie_name,
                release_year=release_year
            )

            message = f"Movie saved: {movie_name} ({release_year})"

            return render(
                request,
                'success.html',
                {'message': message}
            )

    else:
        form = MovieForm()

    return render(
        request,
        'movie_form.html',
        {'form': form}
    )