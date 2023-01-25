from django.forms import ModelForm
from .models import Page
from ckeditor.fields import RichTextField


class PageForm(ModelForm):
    editorContent = RichTextField(config_name='default')
    class Meta:
        model = Page
        fields = ['content']
        labels = {'content':''}