from django.contrib import admin

# Register your models here.

from django.contrib import admin

from webdev.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    # pk:索引
    # 属性list_display表示要显示哪些属性
    list_display = ['pk', 'title', 'body', 'timestamp']


admin.site.register(BlogPost)
