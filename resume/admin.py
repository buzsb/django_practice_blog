from django.contrib import admin
from .models import Resume, Languages, LanguageLevel


class LanguageLevel(admin.TabularInline):
    model = LanguageLevel
    extra = 1


class ResumeAdmin(admin.ModelAdmin):
    inlines = (LanguageLevel,)


class LanguagesAdmin(admin.ModelAdmin):
    inlines = (LanguageLevel,)


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Languages, ResumeAdmin)
