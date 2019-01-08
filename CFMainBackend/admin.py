from django.contrib import admin
from CFMainBackend.models import Actor, ActorVideo
from imagekit.admin import AdminThumbnail
from .widgets import AdminImageWidget
# Register your models here.
from django.utils.html import format_html

class VideosInLine(admin.TabularInline):
    model = ActorVideo
    extra = 0

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    headshot_tag = AdminThumbnail(image_field='headshot')
    list_display = ['name', 'headshot_tag', "_videos"]

    inlines = [
        VideosInLine
    ]

    def _videos(self, obj):
        return obj.videos.all().count()
    # (2) Show thumbnail in changeview
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'headshot':
            # remove request to avoid "__init__() got an unexpected keyword argument 'request'" error
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ActorAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(ActorVideo)
