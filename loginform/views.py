from django.shortcuts import render
from .forms import LoginForm

def login_view(request):

    message = ""

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            message = f"Thank you! Your email is {email}"

            return render(
                request,
                'success.html',
                {'message': message}
            )

    else:
        form = LoginForm()

    return render(
        request,
        'login.html',
        {'form': form}
    )