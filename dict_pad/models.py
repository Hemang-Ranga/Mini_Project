from django.db import models
from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaField

class Page(models.Model):
    # content = RichTextField(blank=True,null=True,config_name='default')
    content = FroalaField(null=True)