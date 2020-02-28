from django.db import models
from datetime import datetime



class TutCategory(models.Model):
	tut_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=100)

	class Meta:
		#Remove the `s` item usually added by django
		verbose_name_plural = "categories"

	def __str__(self):
		return self.tut_category

class TutSeries(models.Model):
	tut_series = models.CharField(max_length=200)
	tut_category = models.ForeignKey(TutCategory,default=1, verbose_name="category",on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		#Remove the `s` item usually added by django
		verbose_name_plural = "series"

	def __str__(self):
		return self.tut_series

# Create your models here.
class Tut(models.Model):
	tut_title = models.CharField("Title", max_length=200)
	tut_content = models.TextField("Content")
	tut_published = models.DateTimeField("date published",default=datetime.now())

	tut_series = models.ForeignKey(TutSeries,default=1,verbose_name='Series',on_delete=models.SET_DEFAULT)
	tut_slug = models.CharField(max_length=200,default=1)


	def __str__(self):
		return self.tut_title