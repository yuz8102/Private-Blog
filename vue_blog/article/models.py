from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
	title = models.CharField(max_length=100)
	created = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.title

class Article(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)
	#author取django.contrib.auth.models中的User
	author = models.ForeignKey(
		User,
		null=True,
		on_delete=models.CASCADE,
		related_name='articles'
	)
	category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )

	#使用print时打印的是title，若不设定，默认打印对象地址
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created']

