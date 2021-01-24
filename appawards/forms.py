from django import forms
from .models import Projects, Profile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('project_photo','description','url','uploader','project_name',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio')