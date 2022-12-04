from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class CustomManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='published')

class AddPost1(models.Model):
	Name = models.CharField(max_length=64)
	email = models.EmailField()
	Write_Post = models.TextField()
	image = models.ImageField(null=True, blank=True, upload_to='images/')
	likes = models.ManyToManyField(User, related_name='blog_posts')

	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse('detail',  kwargs={'pk': self.pk})
