from django.forms import ModelForm
from .models import Page
from ckeditor.fields import RichTextField

PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
          'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'inline_style',
          'line_breaker', 'lists', 'paragraph_format', 'paragraph_style', 'save', 'table','quick_insert','image')

class PageForm(ModelForm):
    content = RichTextField(config_name='default')

    def get_content(self):
        return self.content
    class Meta:
        model = Page
        fields = "__all__"
        labels = {'content':""}