from django.db import models

class ResultNumber(models.Model):
	rounds = models.CharField(max_length=1024)
	result = models.CharField(max_length=1024)

	class Meta:
		ordering = ['rounds']

	def __str__(self):
		return '{} - {}'.format(self.rounds, self.result)
