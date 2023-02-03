from django.forms import Form, CharField
from .models import Page
from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaEditor

PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
          'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'inline_style',
          'line_breaker', 'lists', 'paragraph_format', 'paragraph_style', 'save', 'table','quick_insert','image')

class PageForm(Form):
    editorContent = CharField(
        widget=FroalaEditor(plugins=PLUGINS,
        options={}),
        label='',
        required=False,
        )
