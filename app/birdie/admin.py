from django.contrib import admin
from birdie import models

from birdie.models import Post

class  PostAdmin(admin.ModelAdmin):

    model = Post
    list_display = ('excerpt')


    def excerpt(self, obj):
        return obj.get_excerpt(5)

admin.site.register(models.Post, PostAdmin)
