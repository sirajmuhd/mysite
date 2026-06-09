from django import forms

class MovieForm(forms.Form):
    movie_name = forms.CharField(
        max_length=100,
        label="Movie Name"
    )

    release_year = forms.IntegerField(
        label="Release Year"
    )