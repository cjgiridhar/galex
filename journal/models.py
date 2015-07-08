from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES = (
    ('C', 'Cricket'),
    ('H', 'Hockey'),
    ('F', 'Football')
)

class Article(models.Model):
    title = models.CharField(max_length=100, )
    author = models.ForeignKey('auth.User')
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    hero_image = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/hero-no-img.jpg')
    optional_image = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/opt-no-img.jpg')
    body = models.CharField(max_length=1000, default='')

    class Meta:
        ordering = ('-pub_date', )

