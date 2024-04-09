from django.contrib import admin
from news.models import News, Tag


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_tags',)
    list_display_links = ('id', 'title',)
    readonly_fields = ('likes', 'dislikes', 'views_count',)

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
