from django.contrib import admin
from django.http import HttpRequest

from assignments.models import About, SocialLinks


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLinks)
