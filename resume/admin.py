from django.contrib import admin
from .models import Resume, Language, LanguageLevel


class LanguageLevel(admin.TabularInline):
    model = LanguageLevel
    extra = 1


class ResumeAdmin(admin.ModelAdmin):
    inlines = (LanguageLevel,)


class LanguageAdmin(admin.ModelAdmin):
    inlines = (LanguageLevel,)


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Language, ResumeAdmin)
