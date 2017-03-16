from django.contrib import admin
from .models import Person, Language, LanguageLevel


class LanguageLevel(admin.TabularInline):
    model = LanguageLevel
    extra = 1


class ResumeAdmin(admin.ModelAdmin):
    inlines = (LanguageLevel,)


class LanguageAdmin(admin.ModelAdmin):
    inlines = (LanguageLevel,)


admin.site.register(Person, ResumeAdmin)
admin.site.register(Language, ResumeAdmin)
