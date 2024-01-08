from django.contrib import admin

from educational_modules.models import Lessons


@admin.register(Lessons)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
