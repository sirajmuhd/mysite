from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        error_messages={
            'required': 'Email is required',
            'invalid': 'Enter a valid email address'
        }
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=6,
        error_messages={
            'required': 'Password is required',
            'min_length': 'Password must be at least 6 characters long'
        }
    )

    def clean_email(self):
        email = self.cleaned_data['email']

        if email.endswith('@gmail.com'):
            raise forms.ValidationError(
                "Gmail addresses are not allowed"
            )

        return email