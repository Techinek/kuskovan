from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from tinymce.widgets import TinyMCE

from .models import Post, Category, Tag, Comment

class PostAdminForm(forms.ModelForm):
    """TinyMCE model connected with Post model"""
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):

    """Post model representation in the admin area
     with a form field for TinyMCE model"""
    form = PostAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'published', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', 'category', 'created_at')
    fieldsets = (
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'slug'),
    }),
        ('Main content', {
            'fields': ('title', 'intro_text', 'image', 'content')
    }),
        ('Relations', {
            'fields': ('category', 'tags')
        }),
        ('Promotion', {
            'fields': ('featured', 'published')
        }),
        ('Secondary info', {
            'fields': ('views', 'created_at', 'updated_at',)
        })
    )
    readonly_fields = ('get_image', 'views', 'created_at', 'updated_at',)
    save_on_top = True
    prepopulated_fields = {'seo_description': ('intro_text',)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=75>')
        else:
            return '-'

    get_image.short_description = 'Миниатюра'


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_title', 'published')
    list_display_links = ('id', 'menu_title')
    search_fields = ('title',)
    list_editable = ('published',)
    fieldsets = (
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'slug'),
    }),
        ('Main content', {
            'fields': ('title', 'description')
    }),
        ('Promotion', {
            'fields': ('menu_title', 'published', )
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_title', 'published')
    list_display_links = ('id', 'menu_title')
    search_fields = ('title',)
    list_editable = ('published',)
    fieldsets = (
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'slug'),
    }),
        ('Main content', {
            'fields': ('title', 'description')
    }),
        ('Promotion', {
            'fields': ('menu_title', 'published', )
        }),
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)


