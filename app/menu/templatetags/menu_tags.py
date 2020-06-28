from django import template

from menu.models import MenuItem
from blog.models import Post, Category, Tag, Comment

register = template.Library()

@register.inclusion_tag('menu/tpl/main_menu_tpl.html')
def get_menu_item():
    menu_items = MenuItem.objects.filter(published=True, restricted=False)
    return {'menu_items': menu_items,}