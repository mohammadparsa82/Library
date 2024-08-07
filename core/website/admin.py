from django.contrib import admin
from website.models import Contact, NewLetter
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','created_date')
    list_filter = ('created_date',)
    search_fields = ['name','email']

admin.site.register(Contact, ContactAdmin)
admin.site.register(NewLetter)