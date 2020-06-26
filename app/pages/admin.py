from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Page, Feedback

class PageAdminForm(forms.ModelForm):
    """CKEDITOR model connected with Page model"""
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Page
        fields = '__all__'

class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display = ("title", "published", "id")
    list_editable = ("published",)
    list_filter = ("published",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    actions = ['unpublish', 'publish']
    fieldsets = (
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'slug')
        }),
        ('Main content',{
            'fields': ('title', 'content', )
        }),
        ('Promotion', {
            'fields': ('published', 'created_at',)
        })
    )
    readonly_fields = ('created_at',)
    save_on_top = True

admin.site.register(Page, PageAdmin)
admin.site.register(Feedback)