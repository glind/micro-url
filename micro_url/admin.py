from django.contrib import admin
from .models import URLService


class URLServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(URLService, URLServiceAdmin)