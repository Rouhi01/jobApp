from django.contrib import admin
from .models import Job, Location, Skills, Author


@admin.register(Job)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'salary', 'created_at', '__str__']
    list_filter = ['created_at', 'salary', 'expired_at']
    search_fields = ['title', 'description']
    search_help_text = 'Write your query and hit Enter!'
    exclude = ['created_at']
    prepopulated_fields = {'slug': ['title']}

    fieldsets = (
        ('Basic information', {'fields': (
            'title',
            'description',
        )}),
        ('More information', {
            'fields': (
                ('salary', 'expired_at'),
                'slug'),
            'classes': ('collapse', 'wide')
        })
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
