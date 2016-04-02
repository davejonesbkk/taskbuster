# _*_ coding: UTF-8 _*_

from django.contrib import admin
from . import models

class ProjectsInLine(admin.TabularInline):
	model = models.Project
	extra = 5


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

	list_display = ("username", "interaction", "_projects")

	search_fields = ["user__username"]

	inlines = [
		ProjectsInLine
	]

	
	def _projects(self, obj):
		return obj.projects.all().count()





