from django.contrib import admin
from blogs.models import Post , Category , comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name_book','author','counted_view','status','image','published_date','created_date' )
    list_filter = ('author','status','image','published_date')
    search_fields = ['name_book','author']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display =('name','post','approved','created_date')
    list_filter = ('post','approved',)
    search_fields = ('name','post')

admin.site.register(comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)