# blog/admin.py

from django.contrib import admin
from .models import Post, Subject, StudyMaterial, PreviousYearQuestion, Announcement

class StudyMaterialInline(admin.TabularInline):
    model = StudyMaterial
    extra = 1

class PreviousYearQuestionInline(admin.TabularInline):
    model = PreviousYearQuestion
    extra = 1

class SubjectAdmin(admin.ModelAdmin):
    inlines = [StudyMaterialInline, PreviousYearQuestionInline]

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author')
    fields = ('title', 'content', 'date_posted', 'author', 'image_url')

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'link')
    search_fields = ['name']

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subject, SubjectAdmin)
