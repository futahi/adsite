from django.db import models
#from django.contrib.author.models import User
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='Blog_media', null=True, blank=True )
	file = models.FileField(upload_to='Blog_media', null=True, blank=True)
	alter = models.CharField(max_length=50, null=True, blank=True )

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-date',)


class IslaminSpb(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='Blog_media', null=True, blank=True )
	file = models.FileField(upload_to='Blog_media', null=True, blank=True)
	alter = models.CharField(max_length=50, null=True, blank=True )

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-date',)

class Family(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='Blog_media', null=True, blank=True )
	file = models.FileField(upload_to='Blog_media', null=True, blank=True)
	alter = models.CharField(max_length=50, null=True, blank=True )

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-date',)

class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='Blog_media', null=True, blank=True )
	file = models.FileField(upload_to='Blog_media', null=True, blank=True)
	alter = models.CharField(max_length=50, null=True, blank=True )

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-date',)

class About(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	image = models.ImageField(upload_to='Blog_media', null=True, blank=True )
	alter = models.CharField(max_length=50, null=True, blank=True )

	def __str__(self):
		return self.title



class Sura(models.Model):
	sura_title = models.CharField(max_length=100)
	sura_content = models.TextField()


	def __str__(self):
		return self.sura_title



class Comment(models.Model):
	name = models.CharField(max_length=50, verbose_name='Имя')
	email = models.EmailField(verbose_name='E-mail')
	body = models.TextField(verbose_name='Комментарии')
	date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return '{} прокомментировал на {}' .format(self.name, self.post, )

	class Meta:
		ordering = ('-date',)

class Fcomment(models.Model):
	name = models.CharField(max_length=50, verbose_name='Имя')
	email = models.EmailField(verbose_name='E-mail')
	body = models.TextField(verbose_name='Комментарии')
	date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return '{} прокомментировал на {}' .format(self.name, self.family, )

	class Meta:
		ordering = ('-date',)	
