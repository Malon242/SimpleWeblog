from django.db import models

# Posts created by admin
class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return self.title


# Comments to posts created by visitors
class Comment(models.Model):
	post = models.ForeignKey(Post,
		on_delete = models.CASCADE,
		related_name='comments')
	name = models.CharField(max_length=50)
	content = models.TextField()
	date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return self.content