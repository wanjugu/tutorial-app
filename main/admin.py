from django.contrib import admin
from .models import Tut,TutSeries,TutCategory
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TutAdmin(admin.ModelAdmin):
	# fields = ["tut_title",
	# 		  "tut_published",
	# 		  "tut_content"]

	fieldsets = [
		("Title/date",{"fields": ["tut_title","tut_published"]}),
		("URL",{"fields": ["tut_slug"]}),
		("series",{"fields": ["tut_series"]}),
		("content",{"fields": ["tut_content"]})
	] 

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(TutSeries)
admin.site.register(TutCategory)

admin.site.register(Tut,TutAdmin)