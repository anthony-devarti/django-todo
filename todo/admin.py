from django.contrib import admin

# Register your models here.

from .models import Todo, Event, Category

admin.site.register(Todo)
admin.site.register(Event)
admin.site.register(Category)
