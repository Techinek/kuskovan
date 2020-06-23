from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

from .models import Menu, MenuItem

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Menu"""
    list_display = ('name', 'restricted', 'published')
    list_filter = ('published',)

@admin.register(MenuItem)
class MenuItemAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name', 'parent', 'menu', 'published')
    list_display_links = ('indented_title',)
    list_filter = ('menu', 'parent', 'published')
    fields = ('name', 'slug', 'sort', 'restricted', 'published', 'menu', 'parent')
    search_fields = ('name', 'parent__name', 'menu__name')
    save_as = True
    list_editable = ('published',)

