from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

#...

class Post(models.Model):
    content = RichTextUploadingField()