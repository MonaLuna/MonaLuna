from django.db import models


# Create your models here.
class Chaertli(models.Model):
	
	created = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.created.strftime("%Y-%m-%d")
