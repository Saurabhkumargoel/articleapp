from django.contrib import admin

# Register your models here.
from posts.models import Author, Catagory, Article

	
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_catagory')

	
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    pass
	
	
#admin.site.register(Article)
#admin.site.register(Author)
admin.site.register(Catagory)