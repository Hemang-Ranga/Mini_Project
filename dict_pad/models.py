from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    content = RichTextField(blank=True,null=True,config_name='default')
