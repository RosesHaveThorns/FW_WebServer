from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	colour = models.CharField(max_length=10)
	score = models.IntegerField()
	timePosted = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.timePosted = timezone.now()
		self.save()

	def __str__(self):
		return self.colour
