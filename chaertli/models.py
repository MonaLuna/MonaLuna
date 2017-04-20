from django.db import models


# Create your models here.
class Chaertli(models.Model):
	
	created = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.created.strftime("%Y-%m-%d")


class Sitae(models.Model):
	
	chaertli = models.ForeignKey(Chaertli)
	loesig = models.BooleanField(default=False)
		