from django.contrib import admin

from materials.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    list_filter = ('title',)
    search_fields = ('title', 'body',)
