from django.contrib import admin
from .models import Task
from django.utils.safestring import mark_safe
from .models import Posts, Post, About


#admin.site.register(Posts)


class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "des", "cover")


admin.site.register(Posts, PostsAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ("titl", "desc", "img")


admin.site.register(About, AboutAdmin)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "task", "get_image")
 #   list_display_links = ("title",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image} width="50" height="50"')

    get_image.short_description = "Изображение"

#admin.site.register(Task, TaskAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "created", "text")


admin.site.register(Post, PostAdmin)


