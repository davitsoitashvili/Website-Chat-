from django import forms
from pages.models import Message


class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Write message"}))

    class Meta:
        model = Message
        fields = ('message',)