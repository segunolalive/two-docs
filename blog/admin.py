from django.contrib import admin
from .models import Post, Comment

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "created_date", "published_date"]
	list_display_links = ["published_date"]
	list_editable = ["title"]
	list_filter = ["title", "text"]
	search_fields = ["title", "text"]
	
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin) # Register your models here.

admin.site.register(Comment)