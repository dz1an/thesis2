# smartscore/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher  # Import the Teacher model

class RegistrationFormWithTeacher(UserCreationForm):
    email = forms.EmailField()
    is_teacher = forms.BooleanField(required=False)  # Add a checkbox for teacher registration

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_teacher']

    def save(self, commit=True):
        user = super().save(commit=False)

        # Check if the user is registering as a teacher
        if self.cleaned_data.get('is_teacher'):
            teacher = Teacher.objects.create(user=user)
            # You might want to add additional fields specific to teachers here

        if commit:
            user.save()
            if self.cleaned_data.get('is_teacher'):
                teacher.save()

        return user
