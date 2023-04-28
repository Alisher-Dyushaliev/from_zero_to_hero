from django.contrib import admin
from .models import Newskg, Purpose, Tag, Tree, Store
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

class NewskgAdminForm(forms.ModelForm):
    info = forms.CharField (widget=CKEditorUploadingWidget())

    class Meta:
        model = Newskg
        fields = '__all__'


class NewskgAdmin (admin.ModelAdmin):
    form = NewskgAdminForm
    list_display = ('title', 'content', 'purpose', 'info', 'created_at', 'updated_at', 'is_published', 'get_photo', 'browsing')
    list_display_links = ('content',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('purpose',)
    fields = ('title', 'content', 'tags', 'purpose', 'info', 'photo', 'get_photo', 'is_published', 'browsing', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'browsing', 'created_at', 'updated_at')
    save_on_top = True
    # save_as = True

    def get_photo (self, obj):
        if obj.photo:
            return mark_safe (f'<img src = "{obj.photo.url}" height="75" width="75">')
        else:
            return '-'

    get_photo.short_description='Image'


class PurposeAdmin (admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


class TagAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register (Newskg, NewskgAdmin)
admin.site.register (Purpose, PurposeAdmin)
admin.site.register (Tag, TagAdmin)
# admin.site.register (Tree, MPTTModelAdmin)
admin.site.register (
    Tree,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register (Store)

admin.site.site_title = 'Django administration'
admin.site.site_header = 'Django administration'